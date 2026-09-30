import { addDays, daysBetween, todayStr } from "./util.js";

export const KEY = "yuwen.v1";

export function emptyStore() {
  return {
    version: 1,
    checkins: [],
    plan: null,
    poems: {},
    mistakes: [],
    badges: [],
    seenPopups: [],
    log: [],
    installDismissed: false,
    mistakeFilter: "all",
  };
}

function normalize(data) {
  const base = emptyStore();
  if (!data || typeof data !== "object") return base;
  return {
    ...base,
    ...data,
    version: 1,
    checkins: Array.isArray(data.checkins) ? data.checkins : [],
    poems: data.poems && typeof data.poems === "object" ? data.poems : {},
    mistakes: Array.isArray(data.mistakes) ? data.mistakes : [],
    badges: Array.isArray(data.badges) ? data.badges : [],
    seenPopups: Array.isArray(data.seenPopups) ? data.seenPopups : [],
    log: Array.isArray(data.log) ? data.log : [],
    plan: data.plan && data.plan.date ? data.plan : null,
  };
}

export function loadStore() {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return emptyStore();
    return normalize(JSON.parse(raw));
  } catch {
    return emptyStore();
  }
}

export function saveStore(store) {
  localStorage.setItem(KEY, JSON.stringify(store));
}

export function ensurePlan(store) {
  const t = todayStr();
  if (!store.plan || store.plan.date !== t) {
    const due = store.mistakes.filter((m) => m.status === "active" && m.nextReview && m.nextReview <= t).length;
    store.plan = {
      date: t,
      reviewNeeded: due > 0,
      poetryTokens: [],
      checkedIn: false,
    };
  }
  return store.plan;
}

export function dueMistakes(store, day = todayStr()) {
  return store.mistakes
    .filter((m) => m.status === "active" && m.nextReview && m.nextReview <= day)
    .sort((a, b) => a.nextReview.localeCompare(b.nextReview) || a.id.localeCompare(b.id));
}

export function reviewSatisfied(store) {
  const plan = ensurePlan(store);
  if (!plan.reviewNeeded) return true;
  return dueMistakes(store).length === 0;
}

export function poetryDone(store) {
  const plan = ensurePlan(store);
  return plan.poetryTokens.length >= 3;
}

export function todayMinutes(store) {
  const plan = ensurePlan(store);
  let n = 0;
  if (plan.reviewNeeded && reviewSatisfied(store)) n += 3;
  if (poetryDone(store)) n += 5;
  return n;
}

export function maybeCheckIn(store) {
  const plan = ensurePlan(store);
  if (plan.checkedIn) return false;
  if (reviewSatisfied(store) && poetryDone(store)) {
    plan.checkedIn = true;
    const t = todayStr();
    if (!store.checkins.includes(t)) store.checkins.push(t);
    awardStreakBadges(store);
    return true;
  }
  return false;
}

export function streakInfo(store) {
  const set = [...new Set(store.checkins)].sort();
  if (!set.length) return { current: 0, longest: 0 };
  let longest = 1;
  let run = 1;
  for (let i = 1; i < set.length; i++) {
    if (daysBetween(set[i - 1], set[i]) === 1) {
      run += 1;
      longest = Math.max(longest, run);
    } else if (daysBetween(set[i - 1], set[i]) > 1) {
      run = 1;
    }
  }
  const last = set[set.length - 1];
  const t = todayStr();
  let current = 0;
  if (last === t || last === addDays(t, -1)) {
    current = 1;
    for (let i = set.length - 1; i > 0; i--) {
      if (daysBetween(set[i - 1], set[i]) === 1) current += 1;
      else break;
    }
  }
  return { current, longest: Math.max(longest, current) };
}

function award(store, id) {
  if (!store.badges.includes(id)) store.badges.push(id);
}

function awardStreakBadges(store) {
  const { current } = streakInfo(store);
  if (current >= 3) award(store, "streak3");
  if (current >= 7) award(store, "streak7");
}

export function poemRec(store, id) {
  if (!store.poems[id]) store.poems[id] = { fill: {}, next: {}, nextCleared: false, orderCleared: false, touched: false };
  if (!store.poems[id].fill) store.poems[id].fill = {};
  if (!store.poems[id].next) store.poems[id].next = {};
  return store.poems[id];
}

export function fillClearedCount(store, poem) {
  const rec = store.poems[poem.id];
  if (!rec || !rec.fill) return 0;
  return poem.lines.reduce((n, _, i) => n + (rec.fill[i] && rec.fill[i].cleared ? 1 : 0), 0);
}

export function stageOf(store, poem) {
  const rec = store.poems[poem.id];
  const cleared = fillClearedCount(store, poem);
  const total = poem.lines.length;
  if (!rec || (!rec.touched && cleared === 0)) return "none";
  const active = store.mistakes.some((m) => m.poemId === poem.id && m.status === "active");
  if (cleared >= total && rec.nextCleared && rec.orderCleared && !active) return "mastered";
  if (cleared >= total) return "known";
  return "learning";
}

export function masteryPercent(store, poem) {
  const total = poem.lines.length || 1;
  const cleared = fillClearedCount(store, poem);
  const rec = store.poems[poem.id] || {};
  if (stageOf(store, poem) === "mastered") return 100;
  let p = Math.round((cleared / total) * 70);
  if (rec.nextCleared) p += 15;
  if (rec.orderCleared) p += 15;
  return Math.max(0, Math.min(100, p));
}

export function isLevelOpen(store, poem, index) {
  if (index <= 0) return true;
  const rec = store.poems[poem.id];
  for (let i = 0; i < index; i++) {
    if (!(rec && rec.fill && rec.fill[i] && rec.fill[i].cleared)) return false;
  }
  return true;
}

export function isNextOpen(store, poem, index) {
  if (index <= 0) return true;
  const rec = store.poems[poem.id];
  for (let i = 0; i < index; i++) {
    if (!(rec && rec.next && rec.next[i] && rec.next[i].cleared)) return false;
  }
  return true;
}

function logOk(store, kind, poemId) {
  store.log.push({ date: todayStr(), kind, poemId, ok: true });
  if (store.log.length > 400) store.log = store.log.slice(-400);
}

export function markPoetryToken(store, token) {
  const plan = ensurePlan(store);
  if (!plan.poetryTokens.includes(token)) plan.poetryTokens.push(token);
}

export function recordFill(store, poem, lineIndex, tries) {
  const rec = poemRec(store, poem.id);
  rec.touched = true;
  const stars = tries <= 1 ? 3 : tries === 2 ? 2 : 1;
  const prev = rec.fill[lineIndex] || { cleared: false, stars: 0, tries: 0 };
  rec.fill[lineIndex] = {
    cleared: true,
    stars: Math.max(prev.stars || 0, stars),
    tries: (prev.tries || 0) + tries,
  };
  logOk(store, "level", poem.id);
  markPoetryToken(store, `fill:${poem.id}:${lineIndex}`);
  award(store, "first");
  const all = poem.lines.every((_, i) => rec.fill[i] && rec.fill[i].cleared);
  let freshBadge = false;
  if (all) {
    const id = `poem:${poem.id}`;
    freshBadge = !store.badges.includes(id);
    award(store, id);
  }
  maybeCheckIn(store);
  return { freshBadge, all };
}

export function recordNext(store, poem, lineIndex, tries) {
  const rec = poemRec(store, poem.id);
  rec.touched = true;
  const stars = tries <= 1 ? 3 : tries === 2 ? 2 : 1;
  const prev = rec.next[lineIndex] || { cleared: false, stars: 0 };
  rec.next[lineIndex] = { cleared: true, stars: Math.max(prev.stars || 0, stars) };
  const pairs = poem.lines.length - 1;
  rec.nextCleared = Array.from({ length: pairs }, (_, i) => rec.next[i] && rec.next[i].cleared).every(Boolean);
  logOk(store, "level", poem.id);
  markPoetryToken(store, `next:${poem.id}:${lineIndex}`);
  award(store, "first");
  if (stageOf(store, poem) === "mastered") award(store, `poem:${poem.id}`);
  maybeCheckIn(store);
  return { done: rec.nextCleared };
}

export function recordOrder(store, poem, tries) {
  const rec = poemRec(store, poem.id);
  rec.touched = true;
  rec.orderCleared = true;
  rec.orderStars = tries <= 1 ? 3 : tries === 2 ? 2 : 1;
  logOk(store, "level", poem.id);
  markPoetryToken(store, `order:${poem.id}`);
  award(store, "first");
  maybeCheckIn(store);
  return { done: true };
}

function awardGrade(store, grade, poems) {
  if (!poems) return;
  const list = poems.filter((p) => p.grade === grade);
  if (!list.length) return;
  const ok = list.every((p) => {
    const stage = stageOf(store, p);
    return stage === "known" || stage === "mastered";
  });
  if (ok) award(store, `grade:${grade}`);
}

export function awardGrades(store, poems) {
  for (const g of [1, 2, 3, 4, 5]) awardGrade(store, g, poems);
}

export function mistakeKey(mode, poemId, lineIndex) {
  return `${mode}:${poemId}:${lineIndex}`;
}

export function addMistake(store, item) {
  const id = mistakeKey(item.mode, item.poemId, item.lineIndex);
  let m = store.mistakes.find((x) => x.id === id);
  const day = todayStr();
  if (!m) {
    m = {
      id,
      category: "poetry",
      mode: item.mode,
      poemId: item.poemId,
      lineIndex: item.lineIndex,
      prompt: item.prompt,
      answer: item.answer,
      createdAt: day,
      correctStreak: 0,
      nextReview: addDays(day, 1),
      status: "active",
      history: [],
    };
    store.mistakes.push(m);
  } else {
    m.prompt = item.prompt;
    m.answer = item.answer;
    m.correctStreak = 0;
    m.status = "active";
    m.nextReview = addDays(day, 1);
    m.graduatedAt = null;
  }
  m.history.push({ date: day, ok: false });
  return m;
}

export function reviewCorrect(store, mistake) {
  const day = todayStr();
  mistake.correctStreak = (mistake.correctStreak || 0) + 1;
  mistake.history.push({ date: day, ok: true });
  if (mistake.correctStreak >= 3) {
    mistake.status = "graduated";
    mistake.nextReview = null;
    mistake.graduatedAt = day;
    award(store, "graduate");
  } else if (mistake.correctStreak === 1) {
    mistake.nextReview = addDays(day, 3);
  } else {
    mistake.nextReview = addDays(day, 7);
  }
  maybeCheckIn(store);
}

export function sortedMistakes(store) {
  const rank = (m) => {
    if (m.status === "graduated") return "9";
    return m.nextReview || "9999-99-99";
  };
  return store.mistakes.slice().sort((a, b) => rank(a).localeCompare(rank(b)) || a.id.localeCompare(b.id));
}

export function levelCountOn(store, iso) {
  return store.log.filter((x) => x.date === iso && x.ok && x.kind === "level").length;
}

export const BADGE_DEFS = [
  { id: "first", name: "第一次闯关", hint: "答对任意一关" },
  { id: "streak3", name: "连续 3 天", hint: "连续打卡 3 天" },
  { id: "streak7", name: "连续 7 天", hint: "连续打卡 7 天" },
  { id: "graduate", name: "错题毕业", hint: "一道错题连续答对 3 次" },
  { id: "grade:1", name: "一年级小诗人", hint: "一年级已核实的诗都会背" },
  { id: "grade:2", name: "二年级小诗人", hint: "二年级已核实的诗都会背" },
  { id: "grade:3", name: "三年级小诗人", hint: "三年级已核实的诗都会背" },
  { id: "grade:4", name: "四年级小诗人", hint: "四年级已核实的诗都会背" },
  { id: "grade:5", name: "五年级小诗人", hint: "五年级已核实的诗都会背" },
];
