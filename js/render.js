import {
  BOOK_NAME,
  CATS,
  GRADE_NAME,
  MODES,
  SOON_MODES,
  STAGE_LABEL,
  esc,
  greeting,
  lastDates,
  todayStr,
  weekDates,
} from "./util.js";
import { allPoems, gradeBooks, poemById } from "./poems.js";
import {
  BADGE_DEFS,
  dueMistakes,
  fillClearedCount,
  isLevelOpen,
  isNextOpen,
  levelCountOn,
  masteryPercent,
  poetryDone,
  reviewSatisfied,
  sortedMistakes,
  stageOf,
  streakInfo,
  todayMinutes,
} from "./store.js";

function buddySvg(mood) {
  const cheer = mood === "cheer" || mood === "proud";
  const oops = mood === "oops";
  const eyes = cheer
    ? `<path d="M50 86 q7-8 14 0" fill="none" stroke="#4a4068" stroke-width="2.2" stroke-linecap="round"/><path d="M78 86 q7-8 14 0" fill="none" stroke="#4a4068" stroke-width="2.2" stroke-linecap="round"/>`
    : `<ellipse cx="57" cy="86" rx="3.2" ry="3.6" fill="#4a4068"/><ellipse cx="85" cy="86" rx="3.2" ry="3.6" fill="#4a4068"/><circle cx="58.2" cy="85" r="1" fill="#fff"/><circle cx="86.2" cy="85" r="1" fill="#fff"/>`;
  const brows = oops
    ? `<path d="M48 76 q8-5 14 1" fill="none" stroke="#4a4068" stroke-width="1.8" stroke-linecap="round"/><path d="M80 77 q8-6 14 0" fill="none" stroke="#4a4068" stroke-width="1.8" stroke-linecap="round"/>`
    : "";
  const mouth = oops
    ? `<ellipse cx="71" cy="100" rx="4" ry="3" fill="none" stroke="#c47b90" stroke-width="1.8"/>`
    : `<path d="M62 98 q9 7 18 0" fill="none" stroke="#c47b90" stroke-width="2" stroke-linecap="round"/>`;
  const spark = cheer
    ? `<path d="M22 34 l2.2 5 5.2 1.6-5.2 2-2.2 5.2-1.8-5.2-5.2-2 5.2-1.6z" fill="#e8c872"/><path d="M112 30 l1.8 4.2 4.4 1.2-4.4 1.8-1.8 4.4-1.6-4.4-4.4-1.8 4.4-1.2z" fill="#b7a0ef"/>`
    : `<path d="M108 36 l1.4 3.2 3.4.8-3.4 1.4-1.4 3.4-1.2-3.4-3.4-1.4 3.4-.8z" fill="#e8c872" opacity=".85"/>`;
  return `<svg class="buddy-svg" viewBox="0 0 142 150" aria-hidden="true"><path d="M28 92 q-16 8-8 28 q10-6 16-2 q2-14-8-26z" fill="#d9cff8" opacity=".85"/><path d="M114 92 q16 8 8 28 q-10-6-16-2 q-2-14 8-26z" fill="#d9cff8" opacity=".85"/><ellipse cx="52" cy="46" rx="11" ry="26" fill="#fffaf6" transform="rotate(-14 52 46)"/><ellipse cx="90" cy="46" rx="11" ry="26" fill="#fffaf6" transform="rotate(14 90 46)"/><ellipse cx="52" cy="48" rx="5.5" ry="16" fill="#f3c5d6" transform="rotate(-14 52 48)"/><ellipse cx="90" cy="48" rx="5.5" ry="16" fill="#f3c5d6" transform="rotate(14 90 48)"/><ellipse cx="71" cy="96" rx="36" ry="32" fill="#fffaf6"/><path d="M64 62 a9 9 0 1 0 10 12 a6.2 6.2 0 1 1-10-12z" fill="#e4c56a"/><ellipse cx="48" cy="100" rx="7" ry="3.6" fill="#f0b7c8" opacity=".75"/><ellipse cx="94" cy="100" rx="7" ry="3.6" fill="#f0b7c8" opacity=".75"/>${brows}${eyes}${mouth}<path d="M56 122 q15 12 30 0 q-6 8-15 6 q-9 2-15-6z" fill="#7d62c9"/>${spark}</svg>`;
}

function gem() {
  return `<svg class="gem" viewBox="0 0 64 72" aria-hidden="true"><polygon points="32,4 56,22 48,66 16,66 8,22" fill="currentColor"/><polygon points="32,4 44,22 32,36 20,22" fill="rgba(255,255,255,.62)"/><polygon points="20,22 32,36 32,66 16,66" fill="rgba(255,255,255,.22)"/><circle cx="32" cy="28" r="2.2" fill="#fff"/></svg>`;
}

function burst() {
  const colors = ["#b7a0ef", "#e8c872", "#f0b7c8", "#7ec8c3", "#fff6d8", "#d4c4f5", "#f7d7a8", "#c5e8ea"];
  const bits = colors.map((color, i) => {
    const angle = (i / colors.length) * Math.PI * 2;
    const dist = 42 + (i % 3) * 16;
    const x = Math.round(Math.cos(angle) * dist);
    const y = Math.round(Math.sin(angle) * dist);
    return `<i style="--x:${x}px;--y:${y}px;background:${color}"></i>`;
  }).join("");
  return `<div class="burst" aria-hidden="true">${bits}</div>`;
}

function mascot(talk, mood = "idle") {
  return `<div class="mascot-row mood-${mood}">${talk ? `<div class="bubble">${esc(talk)}</div>` : ""}<div class="buddy">${buddySvg(mood)}</div></div>`;
}

function stars(n) {
  let html = `<span class="stars" aria-label="${n} 颗星">`;
  for (let i = 1; i <= 3; i++) html += `<i class="star${i <= n ? "" : " off"}"></i>`;
  return html + "</span>";
}

function stageChip(stage) {
  return `<span class="chip stage-${stage}">${STAGE_LABEL[stage]}</span>`;
}

function ring(pct, label) {
  const r = 28;
  const c = 2 * Math.PI * r;
  const dash = (Math.max(0, Math.min(100, pct)) / 100) * c;
  return `<div class="ring" aria-label="${esc(label || "")}${pct}%"><svg viewBox="0 0 72 72"><circle cx="36" cy="36" r="${r}" class="ring-bg"/><circle cx="36" cy="36" r="${r}" class="ring-fg" stroke-dasharray="${dash} ${c}"/></svg><b>${pct}</b></div>`;
}

function topbar(title, back) {
  return `<header class="top"><a class="back" href="${back || "#/home"}" aria-label="返回">‹</a><h1>${esc(title)}</h1></header>`;
}

function knownCount(store, poems) {
  return poems.filter((p) => {
    const s = stageOf(store, p);
    return s === "known" || s === "mastered";
  }).length;
}

export function renderHome(app) {
  const { store } = app;
  const poems = allPoems();
  const streak = streakInfo(store);
  const minutes = todayMinutes(store);
  const due = dueMistakes(store);
  const plan = store.plan;
  const reviewOk = reviewSatisfied(store);
  const poetOk = poetryDone(store);
  const clears = plan ? plan.poetryTokens.length : 0;
  const know = knownCount(store, poems);
  const week = weekDates();
  const today = todayStr();
  const names = ["一", "二", "三", "四", "五", "六", "日"];
  const continueHref = !reviewOk ? "#/review" : "#/poetry";

  const steps = [
    {
      n: "1",
      name: "错题重考",
      time: "3 分钟",
      state: !plan.reviewNeeded ? "skip" : reviewOk ? "done" : "now",
      text: !plan.reviewNeeded ? "今天没有" : reviewOk ? "做完了" : `${due.length} 道要复习`,
      href: "#/review",
    },
    {
      n: "2",
      name: "古诗词",
      time: "5 分钟",
      state: poetOk ? "done" : reviewOk ? "now" : "todo",
      text: poetOk ? `已闯 ${clears} 关` : `${clears} / 3 关`,
      href: "#/poetry",
    },
    { n: "3", name: "阅读理解", time: "5 分钟", state: "soon", text: "即将上线", href: "#/soon/reading" },
    { n: "4", name: "快问快答", time: "2 分钟", state: "soon", text: "即将上线", href: "#/soon/literature" },
  ];

  return `
    <div class="land-split">
      <section>
        <div class="hello">
          <div>
            <p class="greet">${esc(greeting())}</p>
            <h2>今天也来读一首诗</h2>
            <p class="sub">连续打卡 <b>${streak.current}</b> 天${streak.longest ? ` · 最长 ${streak.longest} 天` : ""}</p>
          </div>
          ${mascot("读一首吧", "idle")}
        </div>
        <div class="week" aria-label="本周打卡">
          ${week.map((d, i) => `<div class="day${d === today ? " today" : ""}${store.checkins.includes(d) ? " on" : ""}"><i>${store.checkins.includes(d) ? "✦" : ""}</i><span>${names[i]}</span></div>`).join("")}
        </div>
        <article class="card plan">
          <header><h3>今日 15 分钟</h3><span class="pill">${minutes} / 15 分钟</span></header>
          <ol class="steps">
            ${steps.map((s) => `<li class="step ${s.state}"><a href="${s.href}"><em>${s.n}</em><span><b>${esc(s.name)}</b><small>${esc(s.time)} · ${esc(s.text)}</small></span></a></li>`).join("")}
          </ol>
          <a class="btn block" href="${continueHref}">${poetOk && reviewOk ? "今天的计划完成了" : "继续今天的计划"}</a>
        </article>
      </section>
      <section>
        <h3 class="sec-title">五类练习</h3>
        <div class="cat-grid">
          ${CATS.map((c) => {
            const extra = c.id === "poetry" ? `${know}/${poems.length} 首会背` : "还在准备";
            return `<a class="card cat" href="${c.href}" style="--cat:${c.color};--soft:${c.soft}"><i class="dot"></i><span><b>${esc(c.name)}</b><small>${extra}</small></span>${c.live ? "" : `<em class="soon-tag">即将上线</em>`}</a>`;
          }).join("")}
          <div class="card cat dashed"><i class="dot" style="background:#C9C2B8"></i><span><b>表达习作素材积累</b><small>即将上线</small></span><em class="soon-tag">即将上线</em></div>
        </div>
      </section>
    </div>`;
}

export function renderPoetry(app) {
  const { store } = app;
  const poems = allPoems();
  const lines = poems.reduce((n, p) => n + p.lines.length, 0);
  const fillDone = poems.reduce((n, p) => n + fillClearedCount(store, p), 0);
  const nextDone = poems.filter((p) => store.poems[p.id] && store.poems[p.id].nextCleared).length;
  const orderDone = poems.filter((p) => store.poems[p.id] && store.poems[p.id].orderCleared).length;
  const cards = [
    { ...MODES.fill, href: "#/grades/fill", stat: `${fillDone}/${lines} 句` },
    { ...MODES.next, href: "#/grades/next", stat: `${nextDone}/${poems.length} 首` },
    { ...MODES.order, href: "#/grades/order", stat: `${orderDone}/${poems.length} 首` },
    ...SOON_MODES.map((m) => ({ ...m, href: `#/soon/mode-${m.id}`, stat: "即将上线", soon: true })),
  ];
  return `${topbar("古诗词", "#/home")}
    <p class="lead">选一种练法。</p>
    <div class="list">
      ${cards.map((c) => `<a class="card row-card" href="${c.href}"><span><b>${esc(c.name)}</b><small>${esc(c.blurb)}</small></span><em class="${c.soon ? "soon-tag" : "count-tag"}">${esc(c.stat)}</em></a>`).join("")}
    </div>`;
}

export function renderSoon(title) {
  return `${topbar(title || "即将上线", "#/home")}
    <article class="card empty">
      ${mascot("还在准备", "idle")}
      <h2>即将上线</h2>
      <a class="btn" href="#/poetry">去练古诗词</a>
    </article>`;
}

export function renderGrades(app, mode) {
  const info = MODES[mode];
  if (!info) return renderSoon("即将上线");
  return `${topbar(info.name, "#/poetry")}
    <p class="lead">${esc(info.blurb)}</p>
    <div class="grade-grid">
      ${[1, 2, 3, 4, 5].map((g) => {
        const books = gradeBooks(g);
        const poems = books.flatMap((b) => b.poems);
        const know = knownCount(app.store, poems);
        return `<a class="card grade" href="#/grade/${mode}/${g}"><b>${GRADE_NAME[g]}</b><small>${poems.length ? `${know}/${poems.length} 首会背` : "篇目未核实"}</small></a>`;
      }).join("")}
    </div>`;
}

export function renderGrade(app, mode, grade) {
  const g = Number(grade);
  const info = MODES[mode];
  if (!info || !GRADE_NAME[g]) return renderSoon("找不到这一页");
  const books = gradeBooks(g);
  const note = g === 4 || g === 5 ? `<p class="note">${GRADE_NAME[g]}下册新版还没有收录。</p>` : "";
  return `${topbar(`${GRADE_NAME[g]} · ${info.name}`, `#/grades/${mode}`)}
    ${note}
    ${books.map((b) => `<section class="book"><h3>${GRADE_NAME[g]}${BOOK_NAME[b.book]}</h3>
      ${b.pending.map((u) => `<div class="card poem unverified"><span><b>${esc(u.title)}</b><small>未核实</small></span><em class="soon-tag">未核实</em><p>${esc(u.reason)}</p></div>`).join("")}
      <div class="poem-grid">
        ${b.poems.map((p) => poemCard(app, p, mode)).join("")}
      </div>
    </section>`).join("")}
    ${books.length ? "" : `<article class="card empty"><h2>这一册还没有可练的诗</h2></article>`}`;
}

function poemCard(app, poem, mode) {
  const stage = stageOf(app.store, poem);
  const pct = masteryPercent(app.store, poem);
  const sub = poem.subtitle ? `<small>${esc(poem.subtitle)}</small>` : "";
  return `<a class="card poem" href="#/path/${mode}/${poem.id}">
    ${ring(pct, poem.title)}
    <span><b>${esc(poem.title)}</b>${sub}<small>${esc(poem.dynasty)} · ${esc(poem.author)}</small></span>
    ${stageChip(stage)}
  </a>`;
}

export function renderPath(app, mode, poemId) {
  const poem = poemById(poemId);
  const info = MODES[mode];
  if (!poem || !info) return renderSoon("这首诗还不在题库里");
  const rec = app.store.poems[poem.id] || { fill: {}, next: {} };
  let nodes = "";
  let startHref = "";
  if (mode === "fill") {
    nodes = poem.lines.map((line, i) => {
      const open = isLevelOpen(app.store, poem, i);
      const cleared = rec.fill && rec.fill[i] && rec.fill[i].cleared;
      const st = cleared ? rec.fill[i].stars : 0;
      const href = open ? `#/quiz/fill/${poem.id}/${i}` : "";
      return nodeHtml(i, `第 ${i + 1} 关`, line, open, cleared, st, href);
    }).join("");
    const next = poem.lines.findIndex((_, i) => !(rec.fill && rec.fill[i] && rec.fill[i].cleared));
    const index = next === -1 ? 0 : next;
    startHref = isLevelOpen(app.store, poem, index) ? `#/quiz/fill/${poem.id}/${index}` : `#/quiz/fill/${poem.id}/0`;
  } else if (mode === "next") {
    nodes = poem.lines.slice(0, -1).map((line, i) => {
      const open = isNextOpen(app.store, poem, i);
      const cleared = rec.next && rec.next[i] && rec.next[i].cleared;
      const st = cleared ? rec.next[i].stars : 0;
      const href = open ? `#/quiz/next/${poem.id}/${i}` : "";
      return nodeHtml(i, `第 ${i + 1} 关`, `${line} → ?`, open, cleared, st, href);
    }).join("");
    const next = poem.lines.slice(0, -1).findIndex((_, i) => !(rec.next && rec.next[i] && rec.next[i].cleared));
    const index = next === -1 ? 0 : next;
    startHref = `#/quiz/next/${poem.id}/${index}`;
  } else {
    const cleared = !!rec.orderCleared;
    nodes = nodeHtml(0, "排序关", "把诗句排回原顺序", true, cleared, rec.orderStars || 0, `#/quiz/order/${poem.id}/0`);
    startHref = `#/quiz/order/${poem.id}/0`;
  }
  const stage = stageOf(app.store, poem);
  return `${topbar(poem.title, `#/grade/${mode}/${poem.grade}`)}
    <div class="land-split">
      <section>
        <p class="lead">${esc(poem.dynasty)} · ${esc(poem.author)}${poem.subtitle ? ` · ${esc(poem.subtitle)}` : ""}</p>
        <div class="path">${nodes}</div>
      </section>
      <aside class="card side-card">
        <p>${stageChip(stage)} ${ring(masteryPercent(app.store, poem), poem.title)}</p>
        <h3>${esc(info.name)}</h3>
        <p class="sub">逐句过关，收下这首诗的徽章。</p>
        <a class="btn block" href="${startHref}">${fillClearedCount(app.store, poem) ? "继续闯关" : "开始"}</a>
      </aside>
    </div>`;
}

function nodeHtml(i, title, line, open, cleared, starCount, href) {
  const cls = `path-node${cleared ? " cleared" : ""}${open ? "" : " locked"}`;
  const inner = `<span class="bubble-n">${i + 1}</span><span><b>${esc(title)}</b><small>${esc(line)}</small>${cleared ? stars(starCount) : ""}</span>`;
  if (!open) return `<div class="${cls}">${inner}<em>未解锁</em></div>`;
  return `<a class="${cls}" href="${href}">${inner}<em>${cleared ? "已过关" : "去闯关"}</em></a>`;
}

export function renderQuiz(app) {
  const q = app.quiz;
  if (q && q.blocked) {
    return `${topbar("还没解锁", q.back)}<article class="card empty"><h2>先完成上一关</h2><p>过关之后，下一句才会打开。</p><a class="btn" href="${esc(q.back)}">回到关卡</a></article>`;
  }
  if (!q || q.missing) return renderSoon("题目还没准备好");
  const poem = poemById(q.poemId);
  if (!poem) return renderSoon("这首诗还不在题库里");
  const back = `#/path/${q.mode}/${poem.id}`;
  let body = "";
  if (q.mode === "fill") {
    body = fillBody(q, poem);
  } else if (q.mode === "next") {
    body = nextBody(q, poem);
  } else {
    body = orderBody(q, poem);
  }
  const foot = feedback(q);
  return `${topbar(`${poem.title} · 第 ${q.label} 关`, back)}
    <div class="land-split quiz">
      <section class="card poem-card kai">${body}</section>
      <section class="quiz-side">
        ${mascot(
          q.phase === "correct" ? "这句是你的了" : q.phase === "wrong" ? "再看一眼" : (q.mode === "next" ? "接上下一句" : q.mode === "order" ? "排回原来的样子" : "填上这句"),
          q.phase === "correct" ? "cheer" : q.phase === "wrong" ? "oops" : "idle"
        )}
        ${q.mode === "fill" ? choicesHtml(q) : ""}
        ${foot}
      </section>
    </div>
    ${app.modal ? modalHtml(app) : ""}`;
}

function fillBody(q, poem) {
  const prev = poem.lines.slice(0, q.lineIndex).map((line) => `<p class="prev">${esc(line)}</p>`).join("");
  let current = "";
  let bi = 0;
  for (let i = 0; i < q.text.length; i++) {
    if (q.blanks.includes(i)) {
      const ch = q.picked[bi] || "";
      current += `<button type="button" class="blank${ch ? " filled" : ""}" data-act="clear-blank" data-i="${bi}">${ch ? esc(ch) : ""}</button>`;
      bi += 1;
    } else {
      current += `<span>${esc(q.text[i])}</span>`;
    }
  }
  return `${prev}<p class="now">${current}</p><p class="gate">第 ${q.lineIndex + 1} 关 / 共 ${poem.lines.length} 关</p>`;
}

function choicesHtml(q) {
  return `<div class="choices">${q.choices.map((ch) => `<button type="button" class="choice" data-act="pick-char" data-ch="${esc(ch)}" ${q.phase === "answer" ? "" : "disabled"}>${esc(ch)}</button>`).join("")}</div>`;
}

function nextBody(q, poem) {
  const opts = q.options.map((line, i) => `<button type="button" class="opt${q.selected === i ? " on" : ""}" data-act="pick-opt" data-i="${i}" ${q.phase === "answer" ? "" : "disabled"}>${esc(line)}</button>`).join("");
  return `<p class="eyebrow">上句</p><p class="now">${esc(poem.lines[q.lineIndex])}</p><p class="eyebrow">下一句是哪一句？</p><div class="opts">${opts}</div>`;
}

function orderBody(q) {
  const slots = q.placed.map((item, i) => `<button type="button" class="slot" data-act="unplace" data-i="${i}" ${q.phase === "answer" ? "" : "disabled"}>${esc(item.text)}</button>`).join("");
  const rest = q.chips.map((item, i) => `<button type="button" class="chip-line" data-act="place" data-i="${i}" ${q.phase === "answer" ? "" : "disabled"}>${esc(item.text)}</button>`).join("");
  return `<p class="eyebrow">按原来的顺序排好</p><div class="slots">${slots || `<span class="hint">排到这里</span>`}</div><div class="chips">${rest}</div>`;
}

function feedback(q) {
  if (q.phase === "answer") {
    return `<div class="quiz-foot"><button type="button" class="btn block" data-act="check">检查</button></div>`;
  }
  if (q.phase === "correct") {
    const label = q.fromReview ? "继续复习" : q.hasNext ? "下一关" : "回到关卡";
    const extra = !q.fromReview && q.mode === "fill" && q.finishedPoem ? "这首诗的逐句填空通关了。" : "";
    return `<div class="quiz-foot ok">${burst()}<p>答对了。${extra}</p><button type="button" class="btn block" data-act="next-step">${label}</button></div>`;
  }
  return `<div class="quiz-foot bad"><p>正确是：<b class="kai">${esc(q.answerText)}</b></p><p>已经放进错题本。</p><button type="button" class="btn block ghost" data-act="retry">再试一次</button></div>`;
}

function modalHtml(app) {
  const m = app.modal;
  return `<div class="mask" role="dialog" aria-modal="true"><div class="card pop">${burst()}${mascot("这块水晶给你", "proud")}<div class="badge-medal">${gem()}</div><h2>得到徽章</h2><p>${esc(m.title)}</p><button type="button" class="btn" data-act="close-modal">收下</button><a class="text-link" href="#/badges">去徽章墙</a></div></div>`;
}

export function renderReviewList(app) {
  const due = dueMistakes(app.store);
  if (!due.length) {
    return `${topbar("今天的重考", "#/home")}
      <article class="card empty">${mascot("今天清清爽爽", "proud")}<h2>今天没有要复习的题</h2><a class="btn" href="#/poetry">去闯关</a></article>`;
  }
  return `${topbar(`今天要复习 · ${due.length}`, "#/home")}
    <div class="list">${due.map((m) => mistakeCard(app, m, true)).join("")}</div>`;
}

export function renderMistakes(app) {
  const filter = app.store.mistakeFilter || "all";
  const all = sortedMistakes(app.store);
  const filters = [["all", "全部"], ["poetry", "古诗词"], ["dictation", "听写"], ["reading", "阅读"], ["idiom", "成语"], ["literature", "常识"]];
  const list = all.filter((m) => filter === "all" || m.category === filter);
  const today = todayStr();
  const groups = [
    ["今天要复习", list.filter((m) => m.status === "active" && m.nextReview && m.nextReview <= today)],
    ["待复习", list.filter((m) => m.status === "active" && m.nextReview && m.nextReview > today)],
    ["已毕业", list.filter((m) => m.status === "graduated")],
  ];
  const other = filter !== "all" && filter !== "poetry";
  return `${topbar("错题本", "#/home")}
    <div class="filters">${filters.map(([id, name]) => `<button type="button" class="${filter === id ? "on" : ""}" data-act="filter" data-id="${id}">${name}</button>`).join("")}</div>
    ${other ? `<article class="card empty"><h2>即将上线</h2></article>` : ""}
    ${!other && !list.length ? `<article class="card empty">${mascot("还是空的", "idle")}<h2>还没有错题</h2></article>` : ""}
    ${!other ? groups.filter((g) => g[1].length).map(([name, items]) => `<section><h3 class="sec-title">${name} · ${items.length}</h3><div class="list">${items.map((m) => mistakeCard(app, m)).join("")}</div></section>`).join("") : ""}`;
}

function mistakeCard(app, m, review) {
  const poem = poemById(m.poemId);
  const title = poem ? poem.title : "古诗词";
  const when = m.status === "graduated" ? `已于 ${m.graduatedAt || ""} 毕业` : `复习日 ${m.nextReview} · 已连续答对 ${m.correctStreak || 0}/3`;
  const href = review || m.status === "active" ? `#/review/${encodeURIComponent(m.id)}` : `#/mistakes`;
  const modeName = m.mode === "next" ? "看上句接下句" : m.mode === "order" ? "诗句排序" : "逐句填空";
  const which = m.lineIndex >= 0 ? `第 ${m.lineIndex + 1} 关` : "整首";
  return `<article class="card mistake"><header><b>${esc(title)}</b><span class="chip c-poem">古诗词</span></header><p>${esc(which)} · ${modeName}</p><small>${esc(when)}</small>${m.status === "active" ? `<a class="btn small" href="${href}">去重练</a>` : ""}</article>`;
}

export function renderBadges(app) {
  const { store } = app;
  const poems = allPoems();
  const poemBadges = poems.map((p) => ({
    id: `poem:${p.id}`,
    name: `${p.title}通关`,
    hint: "逐句填空全部过关",
  }));
  const defs = BADGE_DEFS.concat(poemBadges);
  const got = defs.filter((d) => store.badges.includes(d.id)).length;
  return `${topbar("徽章墙", "#/me")}
    <p class="lead">已获得 ${got} / ${defs.length}</p>
    <div class="badge-grid">
      ${defs.map((d) => {
        const on = store.badges.includes(d.id);
        return `<div class="card badge${on ? " on" : ""}"><div class="badge-medal">${gem()}</div><b>${esc(d.name)}</b><small>${on ? "已获得" : esc(d.hint)}</small></div>`;
      }).join("")}
    </div>`;
}

export function renderProgress(app) {
  const { store } = app;
  const poems = allPoems();
  const streak = streakInfo(store);
  const stages = { none: 0, learning: 0, known: 0, mastered: 0 };
  for (const p of poems) stages[stageOf(store, p)] += 1;
  const days = lastDates(7);
  const counts = days.map((d) => levelCountOn(store, d));
  const max = Math.max(1, ...counts);
  const active = store.mistakes.filter((m) => m.status === "active").length;
  const graduated = store.mistakes.filter((m) => m.status === "graduated").length;
  return `${topbar("进度", "#/me")}
    <div class="land-split">
      <section class="card pad">
        <h3>连续打卡 ${streak.current} 天</h3>
        <p class="sub">最长 ${streak.longest} 天</p>
        <div class="week" aria-label="本周打卡">
          ${weekDates().map((d, i) => `<div class="day${d === todayStr() ? " today" : ""}${store.checkins.includes(d) ? " on" : ""}"><i>${store.checkins.includes(d) ? "✦" : ""}</i><span>${"一二三四五六日"[i]}</span></div>`).join("")}
        </div>
        <p class="sub">错题本：还在复习 ${active} · 已毕业 ${graduated}</p>
        <a class="text-link" href="#/mistakes">打开错题本</a>
      </section>
      <section>
        <article class="card pad">
          <h3>星阶</h3>
          <ul class="stage-list">
            <li><span class="chip stage-none">${STAGE_LABEL.none}</span><b>${stages.none}</b></li>
            <li><span class="chip stage-learning">${STAGE_LABEL.learning}</span><b>${stages.learning}</b></li>
            <li><span class="chip stage-known">${STAGE_LABEL.known}</span><b>${stages.known}</b></li>
            <li><span class="chip stage-mastered">${STAGE_LABEL.mastered}</span><b>${stages.mastered}</b></li>
          </ul>
          ${[1, 2, 3, 4, 5].map((g) => {
            const list = poems.filter((p) => p.grade === g);
            const know = knownCount(store, list);
            const pct = list.length ? Math.round((know / list.length) * 100) : 0;
            return `<div class="bar-row"><span>${GRADE_NAME[g]}</span><span class="bar"><i style="width:${pct}%"></i></span><em>${know}/${list.length}</em></div>`;
          }).join("")}
        </article>
        <article class="card pad">
          <h3>近 7 天闯关</h3>
          <div class="bars">${days.map((d, i) => `<div><span style="height:${Math.max(4, (counts[i] / max) * 72)}px"></span><small>${counts[i]}</small><em>${d.slice(5)}</em></div>`).join("")}</div>
        </article>
        <div class="poem-grid mini">
          ${poems.map((p) => `<a class="card poem mini" href="#/path/fill/${p.id}">${ring(masteryPercent(store, p), p.title)}<span><b>${esc(p.title)}</b>${stageChip(stageOf(store, p))}</span></a>`).join("")}
        </div>
      </section>
    </div>`;
}

export function renderMe(app) {
  const { store } = app;
  const poems = allPoems();
  const streak = streakInfo(store);
  const got = store.badges.length;
  const know = knownCount(store, poems);
  return `${topbar("我的", "#/home")}
    <div class="stat-row">
      <div class="card stat"><b>${streak.current}</b><small>连续打卡</small></div>
      <div class="card stat"><b>${know}/${poems.length}</b><small>诗会背</small></div>
      <div class="card stat"><b>${got}</b><small>徽章</small></div>
    </div>
    <div class="list">
      <a class="card row-card" href="#/progress"><span><b>进度</b><small>星尘到星河诗仙</small></span></a>
      <a class="card row-card" href="#/badges"><span><b>徽章墙</b><small>已获得 ${got} 枚</small></span></a>
    </div>
    <p class="foot-quiet"><a href="#/backup">备份</a></p>`;
}

export function renderBackup() {
  return `${topbar("备份", "#/me")}
    <article class="card pad backup-card">
      <button type="button" class="btn" data-act="export">导出备份</button>
      <button type="button" class="btn ghost" data-act="pick-import">导入备份</button>
      <input id="import-file" type="file" accept="application/json,.json" hidden>
    </article>`;
}

export function renderTab(route) {
  const tab = tabOf(route);
  const items = [
    ["home", "首页", "家"],
    ["play", "闯关", "关"],
    ["mistakes", "错题本", "错"],
    ["me", "我的", "我"],
  ];
  return items.map(([id, name, glyph]) => {
    const href = id === "home" ? "#/home" : id === "play" ? "#/poetry" : id === "mistakes" ? "#/mistakes" : "#/me";
    return `<a href="${href}" class="${tab === id ? "on" : ""}"><b>${glyph}</b><span>${name}</span></a>`;
  }).join("");
}

function tabOf(route) {
  const head = route[0] || "home";
  if (head === "mistakes" || head === "review") return "mistakes";
  if (["me", "badges", "progress", "install", "backup"].includes(head)) return "me";
  if (head === "home") return "home";
  return "play";
}

export function renderRoute(app, route) {
  const [head, a, b, c] = route;
  switch (head) {
    case "home":
      return renderHome(app);
    case "poetry":
      return renderPoetry(app);
    case "soon":
      return renderSoon("即将上线");
    case "grades":
      return renderGrades(app, a);
    case "grade":
      return renderGrade(app, a, b);
    case "path":
      return renderPath(app, a, b);
    case "quiz":
    case "review":
      if (head === "review" && !a) return renderReviewList(app);
      return renderQuiz(app);
    case "mistakes":
      return renderMistakes(app);
    case "badges":
      return renderBadges(app);
    case "progress":
      return renderProgress(app);
    case "me":
      return renderMe(app);
    case "install":
      return renderMe(app);
    case "backup":
      return renderBackup();
    default:
      return renderHome(app);
  }
}
