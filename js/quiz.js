import { hashSeed, seededShuffle } from "./util.js";

const POOL = "春夏秋冬风花雪月山水石林云雨霜露鸟鱼舟车星辉暗左右高低远近大小中外天地人思故乡看望举头低床荷莲叶红绿碧青黄白紫柳梅竹松江河湖波涛浪沙桥寺钟声夜半愁眠枫渔火乌啼落满天街小雨润如酥草色遥看近却无最一年好处皇都残阳铺水瑟可怜九月初三夜露弓横岭侧峰识真面目缘身在此山中童遥指杏花村酒家何处有行人欲断魂清明时节纷纷爆竹声岁除暖入屠苏千门万户日新桃换旧符独异乡客每逢佳节倍亲兄弟登高处遍插少一人";

const AVOID = {
  元: "原",
  材: "才",
  阁: "搁",
  阴: "荫",
  泛: "汛",
  真: "珍",
  珠: "珠",
  绦: "淘",
  蓑: "衰",
  蒌: "芦",
  熏: "薰",
  暝: "瞑",
  盖: "罩",
};

export function hanIndexes(text) {
  const out = [];
  for (let i = 0; i < text.length; i++) {
    if (/[\u4e00-\u9fff]/.test(text[i])) out.push(i);
  }
  return out;
}

export function blankIndexes(text) {
  const idxs = hanIndexes(text);
  if (!idxs.length) return [];
  if (idxs.length <= 2) return [idxs[idxs.length - 1]];
  const a = idxs[Math.min(2, idxs.length - 1)];
  const b = idxs[idxs.length - 1];
  return a === b ? [a] : [a, b];
}

export function makeChoices(text, blanks, seedKey) {
  const answers = blanks.map((i) => text[i]);
  const uniq = [];
  for (const ch of answers) if (!uniq.includes(ch)) uniq.push(ch);
  const ban = new Set(uniq);
  for (const ch of uniq) {
    if (AVOID[ch]) ban.add(AVOID[ch]);
  }
  const extras = [];
  const src = POOL + text;
  for (const ch of src) {
    if (extras.length >= 6 - uniq.length) break;
    if (!/[\u4e00-\u9fff]/.test(ch) || ban.has(ch)) continue;
    ban.add(ch);
    extras.push(ch);
  }
  let n = 0;
  while (extras.length < 6 - uniq.length) {
    const ch = String.fromCharCode(0x4e00 + ((hashSeed(seedKey) + n) % 80));
    n += 1;
    if (ban.has(ch)) continue;
    ban.add(ch);
    extras.push(ch);
    if (n > 200) break;
  }
  return seededShuffle(uniq.concat(extras).slice(0, 6), hashSeed(seedKey));
}

export function nextOptions(poem, lineIndex, corpus, seedKey) {
  const answer = poem.lines[lineIndex + 1];
  const pool = [];
  for (const p of corpus) {
    for (const line of p.lines) {
      if (line !== answer && line !== poem.lines[lineIndex] && !pool.includes(line)) pool.push(line);
    }
  }
  const picked = seededShuffle(pool, hashSeed(seedKey)).slice(0, 2);
  return seededShuffle([answer, ...picked], hashSeed(seedKey + ":o"));
}

export function orderChips(lines, seedKey) {
  return seededShuffle(lines.map((text, index) => ({ text, index })), hashSeed(seedKey));
}
