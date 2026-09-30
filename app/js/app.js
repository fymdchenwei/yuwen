import { loadPoems, poemById, allPoems } from "./poems.js";
import { blankIndexes, makeChoices, nextOptions, orderChips } from "./quiz.js";
import {
  addMistake,
  awardGrades,
  dueMistakes,
  emptyStore,
  ensurePlan,
  isLevelOpen,
  isNextOpen,
  loadStore,
  recordFill,
  recordNext,
  recordOrder,
  reviewCorrect,
  saveStore,
} from "./store.js";
import { renderRoute, renderTab } from "./render.js";
import { todayStr } from "./util.js";

const app = {
  store: emptyStore(),
  quiz: null,
  modal: null,
  swState: "正在注册",
  ios: false,
  standalone: false,
};

const main = document.querySelector("#main");
const tab = document.querySelector("#tab");
const rail = document.querySelector("#rail");

function route() {
  const raw = (location.hash || "#/home").replace(/^#/, "");
  return raw.split("/").filter(Boolean);
}

function toast(msg) {
  const el = document.querySelector("#toast");
  el.textContent = msg;
  el.hidden = false;
  clearTimeout(app.toastTimer);
  app.toastTimer = setTimeout(() => {
    el.hidden = true;
  }, 1700);
}

function persist() {
  ensurePlan(app.store);
  saveStore(app.store);
}

function buildFill(poem, lineIndex, fromReview) {
  if (!fromReview && !isLevelOpen(app.store, poem, lineIndex)) {
    return { blocked: true, back: `#/path/fill/${poem.id}` };
  }
  const text = poem.lines[lineIndex];
  const blanks = blankIndexes(text);
  return {
    key: `fill:${poem.id}:${lineIndex}`,
    mode: "fill",
    poemId: poem.id,
    lineIndex,
    label: lineIndex + 1,
    text,
    blanks,
    choices: makeChoices(text, blanks, `fill:${poem.id}:${lineIndex}`),
    picked: blanks.map(() => ""),
    phase: "answer",
    tries: 0,
    fromReview: !!fromReview,
    answerText: text,
  };
}

function buildNext(poem, lineIndex, fromReview) {
  if (lineIndex < 0 || lineIndex >= poem.lines.length - 1) return { missing: true };
  if (!fromReview && !isNextOpen(app.store, poem, lineIndex)) {
    return { blocked: true, back: `#/path/next/${poem.id}` };
  }
  return {
    key: `next:${poem.id}:${lineIndex}`,
    mode: "next",
    poemId: poem.id,
    lineIndex,
    label: lineIndex + 1,
    text: poem.lines[lineIndex],
    options: nextOptions(poem, lineIndex, allPoems(), `next:${poem.id}:${lineIndex}`),
    selected: null,
    phase: "answer",
    tries: 0,
    fromReview: !!fromReview,
    answerText: poem.lines[lineIndex + 1],
  };
}

function buildOrder(poem, fromReview) {
  return {
    key: `order:${poem.id}`,
    mode: "order",
    poemId: poem.id,
    lineIndex: -1,
    label: 1,
    chips: orderChips(poem.lines, `order:${poem.id}`),
    placed: [],
    phase: "answer",
    tries: 0,
    fromReview: !!fromReview,
    answerText: poem.lines.join(""),
  };
}

function syncQuiz() {
  const r = route();
  if (r[0] === "quiz") {
    const poem = poemById(r[2]);
    const idx = Number(r[3] || 0);
    const key = `${r[1]}:${r[2]}:${idx}`;
    if (!poem) {
      app.quiz = { missing: true };
      return;
    }
    if (!app.quiz || app.quiz.key !== key) {
      if (r[1] === "fill") app.quiz = buildFill(poem, idx, false);
      else if (r[1] === "next") app.quiz = buildNext(poem, idx, false);
      else if (r[1] === "order") app.quiz = buildOrder(poem, false);
      else app.quiz = { missing: true };
    }
    return;
  }
  if (r[0] === "review" && r[1]) {
    const id = decodeURIComponent(r[1]);
    if (!app.quiz || app.quiz.reviewId !== id) app.quiz = buildReview(id);
  }
}

function buildReview(id) {
  const m = app.store.mistakes.find((x) => x.id === id);
  if (!m) return { missing: true };
  const poem = poemById(m.poemId);
  if (!poem) return { missing: true };
  let quiz;
  if (m.mode === "fill") quiz = buildFill(poem, m.lineIndex, true);
  else if (m.mode === "next") quiz = buildNext(poem, m.lineIndex, true);
  else quiz = buildOrder(poem, true);
  if (quiz && !quiz.blocked && !quiz.missing) quiz.reviewId = id;
  return quiz;
}

function render() {
  ensurePlan(app.store);
  syncQuiz();
  const r = route();
  main.innerHTML = renderRoute(app, r);
  const nav = renderTab(r);
  tab.innerHTML = nav;
  rail.innerHTML = nav;
}

function poemOf(q) {
  return poemById(q.poemId);
}

function finishCorrect(q) {
  const poem = poemOf(q);
  let fresh = false;
  if (q.mode === "fill") {
    const result = recordFill(app.store, poem, q.lineIndex, q.tries);
    fresh = result.freshBadge;
    q.hasNext = q.lineIndex + 1 < poem.lines.length;
    q.finishedPoem = result.all;
  } else if (q.mode === "next") {
    const result = recordNext(app.store, poem, q.lineIndex, q.tries);
    q.hasNext = q.lineIndex + 1 < poem.lines.length - 1;
    q.finishedPoem = result.done;
  } else {
    recordOrder(app.store, poem, q.tries);
    q.hasNext = false;
    q.finishedPoem = true;
  }
  if (q.reviewId) {
    const m = app.store.mistakes.find((x) => x.id === q.reviewId);
    if (m) reviewCorrect(app.store, m);
  }
  awardGrades(app.store, allPoems());
  q.phase = "correct";
  if (fresh && !app.store.seenPopups.includes(poem.id)) {
    app.store.seenPopups.push(poem.id);
    app.modal = { title: `${poem.title}通关` };
  }
}

function finishWrong(q) {
  const poem = poemOf(q);
  q.phase = "wrong";
  const prompt = q.mode === "order" ? `${poem.title}诗句排序` : q.mode === "next" ? poem.lines[q.lineIndex] : q.text;
  addMistake(app.store, {
    mode: q.mode,
    poemId: poem.id,
    lineIndex: q.mode === "order" ? -1 : q.lineIndex,
    prompt,
    answer: q.answerText,
  });
  if (q.reviewId) {
    const m = app.store.mistakes.find((x) => x.id === q.reviewId);
    if (m) {
      m.correctStreak = 0;
      m.status = "active";
    }
  }
}

function onCheck() {
  const q = app.quiz;
  if (!q || q.phase !== "answer") return;
  const poem = poemOf(q);
  if (q.mode === "fill") {
    if (q.picked.some((c) => !c)) {
      toast("先把空格填满");
      return;
    }
    const ok = q.blanks.every((index, i) => poem.lines[q.lineIndex][index] === q.picked[i]);
    q.tries += 1;
    if (ok) finishCorrect(q);
    else finishWrong(q);
  } else if (q.mode === "next") {
    if (q.selected == null) {
      toast("先选一句");
      return;
    }
    q.tries += 1;
    if (q.options[q.selected] === poem.lines[q.lineIndex + 1]) finishCorrect(q);
    else finishWrong(q);
  } else {
    if (q.placed.length !== poem.lines.length) {
      toast("先把诗句都排上");
      return;
    }
    q.tries += 1;
    const ok = q.placed.every((item, i) => item.index === i);
    if (ok) finishCorrect(q);
    else finishWrong(q);
  }
  persist();
  render();
}

function onRetry() {
  const q = app.quiz;
  if (!q) return;
  const poem = poemOf(q);
  q.phase = "answer";
  if (q.mode === "fill") q.picked = q.blanks.map(() => "");
  if (q.mode === "next") q.selected = null;
  if (q.mode === "order") {
    q.chips = orderChips(poem.lines, `order:${poem.id}`);
    q.placed = [];
  }
  render();
}

function onNext() {
  const q = app.quiz;
  if (!q) return;
  app.modal = null;
  if (q.hasNext && !q.fromReview) {
    location.hash = `#/quiz/${q.mode}/${q.poemId}/${q.lineIndex + 1}`;
    return;
  }
  if (q.fromReview) {
    const due = dueMistakes(app.store);
    location.hash = due.length ? `#/review/${encodeURIComponent(due[0].id)}` : "#/mistakes";
    return;
  }
  location.hash = `#/path/${q.mode}/${q.poemId}`;
}

function exportBackup() {
  const payload = {
    app: "yuwen",
    version: 1,
    exportedAt: new Date().toISOString(),
    data: app.store,
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `yuwen-backup-${todayStr()}.json`;
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  toast("备份已开始下载");
}

function importBackup(file) {
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const payload = JSON.parse(String(reader.result));
      const data = payload && payload.data ? payload.data : payload;
      if (!data || data.version !== 1 || !data.poems || !Array.isArray(data.mistakes)) {
        toast("这个文件不是本应用的备份");
        return;
      }
      if (!window.confirm("导入会替换这台设备上现在的进度。继续吗？")) return;
      app.store = {
        ...emptyStore(),
        ...data,
        version: 1,
        poems: data.poems,
        mistakes: data.mistakes,
        badges: Array.isArray(data.badges) ? data.badges : [],
        checkins: Array.isArray(data.checkins) ? data.checkins : [],
        log: Array.isArray(data.log) ? data.log : [],
        seenPopups: Array.isArray(data.seenPopups) ? data.seenPopups : [],
      };
      ensurePlan(app.store);
      saveStore(app.store);
      toast("备份已导入");
      render();
    } catch {
      toast("文件读不出来");
    }
  };
  reader.readAsText(file);
}

function onAct(act, dataset) {
  const q = app.quiz;
  if (act === "pick-char" && q && q.phase === "answer") {
    const slot = q.picked.findIndex((c) => !c);
    if (slot === -1) return;
    q.picked[slot] = dataset.ch;
    render();
    return;
  }
  if (act === "clear-blank" && q && q.phase === "answer") {
    const i = Number(dataset.i);
    q.picked[i] = "";
    render();
    return;
  }
  if (act === "pick-opt" && q && q.phase === "answer") {
    q.selected = Number(dataset.i);
    render();
    return;
  }
  if (act === "place" && q && q.phase === "answer") {
    const i = Number(dataset.i);
    const [item] = q.chips.splice(i, 1);
    if (item) q.placed.push(item);
    render();
    return;
  }
  if (act === "unplace" && q && q.phase === "answer") {
    const i = Number(dataset.i);
    const [item] = q.placed.splice(i, 1);
    if (item) q.chips.push(item);
    render();
    return;
  }
  if (act === "check") return onCheck();
  if (act === "retry") return onRetry();
  if (act === "next-step") return onNext();
  if (act === "close-modal") {
    app.modal = null;
    render();
    return;
  }
  if (act === "dismiss-install") {
    app.store.installDismissed = true;
    persist();
    render();
    return;
  }
  if (act === "filter") {
    app.store.mistakeFilter = dataset.id;
    persist();
    render();
    return;
  }
  if (act === "export") return exportBackup();
  if (act === "pick-import") {
    document.querySelector("#import-file")?.click();
  }
}

document.addEventListener("click", (event) => {
  const el = event.target.closest("[data-act]");
  if (!el) return;
  event.preventDefault();
  onAct(el.dataset.act, el.dataset);
});

document.addEventListener("change", (event) => {
  if (event.target && event.target.id === "import-file" && event.target.files && event.target.files[0]) {
    importBackup(event.target.files[0]);
    event.target.value = "";
  }
});

window.addEventListener("hashchange", render);

const orient = matchMedia("(orientation: landscape)");
orient.addEventListener("change", render);

function registerSw() {
  if (!("serviceWorker" in navigator)) {
    app.swState = "浏览器不支持";
    return;
  }
  navigator.serviceWorker
    .register("./sw.js")
    .then((reg) => {
      app.swState = reg.active || reg.installing || reg.waiting ? "已注册" : "已注册";
      render();
    })
    .catch(() => {
      app.swState = "注册失败";
      render();
    });
}

async function boot() {
  const ua = navigator.userAgent || "";
  app.ios = /iPad|iPhone|iPod/.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  app.standalone = matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;
  try {
    await loadPoems();
  } catch (err) {
    main.innerHTML = `<article class="card empty"><h2>诗库没载入</h2><p>${String(err)}</p></article>`;
    return;
  }
  app.store = loadStore();
  ensurePlan(app.store);
  saveStore(app.store);
  if (!location.hash) location.hash = "#/home";
  render();
  registerSw();
}

boot();
