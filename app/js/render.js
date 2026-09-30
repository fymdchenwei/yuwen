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

function mascot(talk) {
  return `<div class="mascot-row">${talk ? `<div class="bubble">${esc(talk)}</div>` : ""}<div class="mascot" aria-hidden="true"><i class="hat"></i><i class="face"><b></b><b></b><s></s></i></div></div>`;
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
      text: !plan.reviewNeeded ? "今天没有到期的错题" : reviewOk ? "今天的重考做完了" : `有 ${due.length} 道今天要复习`,
      href: "#/review",
    },
    {
      n: "2",
      name: "古诗词",
      time: "5 分钟",
      state: poetOk ? "done" : reviewOk ? "now" : "todo",
      text: poetOk ? `今天已闯 ${clears} 关` : `接着闯，满 3 关算完成（已 ${clears} 关）`,
      href: "#/poetry",
    },
    { n: "3", name: "阅读理解", time: "5 分钟", state: "soon", text: "即将上线", href: "#/soon/reading" },
    { n: "4", name: "快问快答", time: "2 分钟", state: "soon", text: "即将上线", href: "#/soon/literature" },
  ];

  const install = installBanner(app);

  return `
    ${install}
    <div class="land-split">
      <section>
        <div class="hello">
          <div>
            <p class="greet">${esc(greeting())}，小朋友</p>
            <h2>今天也来读一首诗</h2>
            <p class="sub">连续打卡 <b>${streak.current}</b> 天${streak.longest ? ` · 最长 ${streak.longest} 天` : ""}</p>
          </div>
          ${mascot("今天从这儿开始")}
        </div>
        <div class="week" aria-label="本周打卡">
          ${week.map((d, i) => `<div class="day${d === today ? " today" : ""}${store.checkins.includes(d) ? " on" : ""}"><i>${store.checkins.includes(d) ? "✓" : ""}</i><span>${names[i]}</span></div>`).join("")}
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

function installBanner(app) {
  if (app.store.installDismissed || app.standalone) return "";
  const ios = app.ios;
  const text = ios
    ? "用 Safari 时，点底部分享按钮，再点「添加到主屏幕」。加上之后，练习记录会更稳。"
    : "可以在浏览器菜单里选择「安装应用」或「添加到主屏幕」，离线也能接着练。";
  return `<aside class="install-banner card"><p><b>添加到主屏幕</b>${esc(text)}</p><span><a href="#/install">看图解</a><button type="button" data-act="dismiss-install">知道了</button></span></aside>`;
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
    <p class="lead">先选一种练法，再选年级和诗。只收录已经核对过正文的诗。</p>
    <div class="list">
      ${cards.map((c) => `<a class="card row-card" href="${c.href}"><span><b>${esc(c.name)}</b><small>${esc(c.blurb)}</small></span><em class="${c.soon ? "soon-tag" : "count-tag"}">${esc(c.stat)}</em></a>`).join("")}
    </div>`;
}

export function renderSoon(title, text) {
  return `${topbar(title || "即将上线", "#/home")}
    <article class="card empty">
      ${mascot("这一块还在准备")}
      <h2>即将上线</h2>
      <p>${esc(text || "这一类练习还没开放。现在可以先练古诗词，答错的句子会自动进错题本。")}</p>
      <a class="btn" href="#/poetry">去练古诗词</a>
    </article>`;
}

export function renderGrades(app, mode) {
  const info = MODES[mode];
  if (!info) return renderSoon("即将上线");
  return `${topbar(info.name, "#/poetry")}
    <p class="lead">${esc(info.blurb)}。点年级看这一册的诗。</p>
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
        <p class="sub">整首逐句填空都过关，会得到这首诗的徽章。</p>
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
        ${mascot(q.phase === "correct" ? "对啦，记住这一句" : q.phase === "wrong" ? "没关系，看正确的再试一次" : "点字填空，再按检查")}
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
  return `<p class="eyebrow">按原来的顺序排好</p><div class="slots">${slots || `<span class="hint">点下面的诗句，排到这里</span>`}</div><div class="chips">${rest}</div>`;
}

function feedback(q) {
  if (q.phase === "answer") {
    return `<div class="quiz-foot"><button type="button" class="btn block" data-act="check">检查</button></div>`;
  }
  if (q.phase === "correct") {
    const label = q.fromReview ? "继续复习" : q.hasNext ? "下一关" : "回到关卡";
    const extra = !q.fromReview && q.mode === "fill" && q.finishedPoem ? "这首诗的逐句填空通关了。" : "";
    return `<div class="quiz-foot ok"><p>答对了。${extra}</p><button type="button" class="btn block" data-act="next-step">${label}</button></div>`;
  }
  return `<div class="quiz-foot bad"><p>正确是：<b class="kai">${esc(q.answerText)}</b></p><p>这道题已经放进错题本，明天会再出现。连续答对 3 次就毕业。</p><button type="button" class="btn block ghost" data-act="retry">再试一次</button></div>`;
}

function modalHtml(app) {
  const m = app.modal;
  return `<div class="mask" role="dialog" aria-modal="true"><div class="card pop"><div class="badge-medal">诗</div><h2>得到徽章</h2><p>${esc(m.title)}</p><button type="button" class="btn" data-act="close-modal">收下</button><a class="text-link" href="#/badges">去徽章墙</a></div></div>`;
}

export function renderReviewList(app) {
  const due = dueMistakes(app.store);
  if (!due.length) {
    return `${topbar("今天的重考", "#/home")}
      <article class="card empty">${mascot("今天没有到期的错题")}<h2>今天没有要复习的题</h2><p>答错的诗句会在明天、3 天后、7 天后回来。连续答对 3 次就毕业。</p><a class="btn" href="#/poetry">去闯关</a></article>`;
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
    ${other ? `<article class="card empty"><h2>即将上线</h2><p>这类练习还没开放，上线后答错的题会出现在这里。</p></article>` : ""}
    ${!other && !list.length ? `<article class="card empty">${mascot("错题本还是空的")}<h2>还没有错题</h2><p>古诗词答错会自动加进来，按复习日期排。新同学这里是 0。</p></article>` : ""}
    ${!other ? groups.filter((g) => g[1].length).map(([name, items]) => `<section><h3 class="sec-title">${name} · ${items.length}</h3><div class="list">${items.map((m) => mistakeCard(app, m)).join("")}</div></section>`).join("") : ""}
    <p class="note">复习间隔：答错后隔天，再对则 3 天后、7 天后。连续 3 次答对就毕业。清除浏览器数据会把错题本一起清掉。</p>`;
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
    <p class="lead">已获得 ${got} / ${defs.length}。没得到的是后面可以拿的目标，不是已经完成的记录。</p>
    <div class="badge-grid">
      ${defs.map((d) => {
        const on = store.badges.includes(d.id);
        return `<div class="card badge${on ? " on" : ""}"><div class="badge-medal">${on ? "诗" : ""}</div><b>${esc(d.name)}</b><small>${on ? "已获得" : esc(d.hint)}</small></div>`;
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
        <p class="sub">最长 ${streak.longest} 天。完成当天可用的计划（错题重考若有，加上古诗词 3 关）算打卡。</p>
        <div class="week" aria-label="本周打卡">
          ${weekDates().map((d, i) => `<div class="day${d === todayStr() ? " today" : ""}${store.checkins.includes(d) ? " on" : ""}"><i>${store.checkins.includes(d) ? "✓" : ""}</i><span>${"一二三四五六日"[i]}</span></div>`).join("")}
        </div>
        <p class="sub">错题本：还在复习 ${active} · 已毕业 ${graduated}</p>
        <a class="text-link" href="#/mistakes">打开错题本</a>
      </section>
      <section>
        <article class="card pad">
          <h3>掌握阶段</h3>
          <ul class="stage-list">
            <li><span class="chip stage-none">不会</span><b>${stages.none}</b></li>
            <li><span class="chip stage-learning">在学</span><b>${stages.learning}</b></li>
            <li><span class="chip stage-known">会了</span><b>${stages.known}</b></li>
            <li><span class="chip stage-mastered">已掌握</span><b>${stages.mastered}</b></li>
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
      <a class="card row-card" href="#/progress"><span><b>进度</b><small>不会、在学、会了、已掌握</small></span></a>
      <a class="card row-card" href="#/badges"><span><b>徽章墙</b><small>已获得 ${got} 枚</small></span></a>
      <a class="card row-card" href="#/install"><span><b>添加到主屏幕</b><small>离线练习更稳</small></span></a>
      <a class="card row-card" href="#/backup"><span><b>导出 / 导入备份</b><small>进度只在这台设备上</small></span></a>
    </div>
    <p class="note">离线缓存：${esc(app.swState)}。清除浏览器数据、或很久不打开，进度和错题本会丢失。换手机前请先导出备份。</p>`;
}

export function renderInstall(app) {
  return `${topbar("添加到主屏幕", "#/me")}
    <article class="card pad">
      <h3>iPhone / iPad（Safari）</h3>
      <ol class="guide"><li>用 Safari 打开这个页面</li><li>点底部分享按钮</li><li>点「添加到主屏幕」</li></ol>
      <h3>安卓（Chrome）</h3>
      <ol class="guide"><li>打开浏览器菜单</li><li>点「安装应用」或「添加到主屏幕」</li></ol>
      <p class="sub">当前：${app.standalone ? "已经从主屏幕打开" : app.ios ? "看起来是 iPhone / iPad 浏览器" : "可以用菜单安装"}。离线缓存 ${esc(app.swState)}。</p>
      <p class="note">进度存在这台设备里。添加到主屏幕后一般更不容易被清掉，但系统仍可能清理长期不用的网站数据。请在「我的」里导出 JSON 备份。</p>
    </article>`;
}

export function renderBackup() {
  return `${topbar("备份", "#/me")}
    <article class="card pad">
      <h3>导出 / 导入</h3>
      <p>备份是一个 JSON 文件，里面是打卡、闯关、错题和徽章。可以换浏览器后再导入。</p>
      <button type="button" class="btn" data-act="export">导出备份</button>
      <button type="button" class="btn ghost" data-act="pick-import">导入备份</button>
      <input id="import-file" type="file" accept="application/json,.json" hidden>
      <p class="note">清除浏览器数据会丢失进度。导入会用文件里的记录替换这台设备上现在的进度。</p>
      <p class="sub"><a href="data/POEMS_SOURCES.md">诗句来源与异文说明</a></p>
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
      return renderSoon("即将上线", soonText(a));
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
      return renderInstall(app);
    case "backup":
      return renderBackup();
    default:
      return renderHome(app);
  }
}

function soonText(id) {
  const map = {
    dictation: "生字词听写还在准备。以后会用系统语音读词，在纸上写，再自己核对。",
    reading: "阅读理解找证据还在准备。正式短文要先核对，再出题。",
    idiom: "成语和近义词还在准备。每个成语会先核对释义再上架。",
    literature: "文学常识速问还在准备。只收录没有争议的题目。",
  };
  if (id && id.startsWith("mode-")) return "这种古诗词练法还在准备，先用逐句填空、接下句和排序。";
  return map[id] || "这一页还在准备。";
}
