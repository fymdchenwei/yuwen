export function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
  }[c]));
}

export function pad(n) {
  return String(n).padStart(2, "0");
}

export function todayStr(date = new Date()) {
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;
}

export function addDays(iso, n) {
  const [y, m, d] = iso.split("-").map(Number);
  const dt = new Date(y, m - 1, d);
  dt.setDate(dt.getDate() + n);
  return todayStr(dt);
}

export function daysBetween(a, b) {
  const [ay, am, ad] = a.split("-").map(Number);
  const [by, bm, bd] = b.split("-").map(Number);
  const da = new Date(ay, am - 1, ad);
  const db = new Date(by, bm - 1, bd);
  return Math.round((db - da) / 86400000);
}

export function weekdayIndex(iso) {
  const [y, m, d] = iso.split("-").map(Number);
  const day = new Date(y, m - 1, d).getDay();
  return day === 0 ? 6 : day - 1;
}

export function weekDates(anchor = todayStr()) {
  const idx = weekdayIndex(anchor);
  const monday = addDays(anchor, -idx);
  return Array.from({ length: 7 }, (_, i) => addDays(monday, i));
}

export function lastDates(n, anchor = todayStr()) {
  return Array.from({ length: n }, (_, i) => addDays(anchor, i - (n - 1)));
}

export function greeting(date = new Date()) {
  const h = date.getHours();
  if (h < 11) return "早上好";
  if (h < 14) return "中午好";
  if (h < 18) return "下午好";
  return "晚上好";
}

export function hashSeed(str) {
  let h = 2166136261;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return h >>> 0;
}

export function seededShuffle(list, seed) {
  const arr = list.slice();
  let s = seed || 1;
  for (let i = arr.length - 1; i > 0; i--) {
    s = (Math.imul(s, 1664525) + 1013904223) >>> 0;
    const j = s % (i + 1);
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export function uid() {
  return `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
}

export const GRADE_NAME = ["", "一年级", "二年级", "三年级", "四年级", "五年级"];
export const BOOK_NAME = { 上: "上册", 下: "下册" };

export const MODES = {
  fill: { id: "fill", name: "逐句遮挡填空", tag: "v1", blurb: "每句一关，过关再开下一句" },
  next: { id: "next", name: "看上句接下句", tag: "v1", blurb: "读上句，选出紧接着的一句" },
  order: { id: "order", name: "诗句排序", tag: "v1", blurb: "把打乱的诗句排回原来的顺序" },
};

export const SOON_MODES = [
  { id: "match", name: "诗题作者连线", blurb: "即将上线" },
  { id: "gloss", name: "字词释义", blurb: "即将上线" },
  { id: "listen", name: "听读跟背", blurb: "即将上线" },
];

export const CATS = [
  { id: "poetry", name: "古诗词", color: "#6D4BD6", soft: "#EDE4FF", href: "#/poetry", live: true },
  { id: "dictation", name: "生字词听写", color: "#3D9A94", soft: "#E5F6F4", href: "#/soon/dictation", live: false },
  { id: "reading", name: "阅读理解找证据", color: "#5BA8C9", soft: "#E7F5FB", href: "#/soon/reading", live: false },
  { id: "idiom", name: "成语与近义词", color: "#D4849A", soft: "#FDECF1", href: "#/soon/idiom", live: false },
  { id: "literature", name: "文学常识速问", color: "#C4A15A", soft: "#FBF6E8", href: "#/soon/literature", live: false },
];

export const STAGE_LABEL = {
  none: "星尘",
  learning: "星光学徒",
  known: "月光诗人",
  mastered: "星河诗仙",
};
