let pack = { poems: [], unverified: [] };

export async function loadPoems() {
  const url = new URL("../data/poems.json", import.meta.url);
  const res = await fetch(url);
  if (!res.ok) throw new Error("诗库读取失败");
  pack = await res.json();
  return pack;
}

export function allPoems() {
  return pack.poems;
}

export function unverified() {
  return pack.unverified || [];
}

export function poemById(id) {
  return pack.poems.find((p) => p.id === id) || null;
}

export function poemsIn(grade, book) {
  return pack.poems.filter((p) => p.grade === grade && (!book || p.book === book));
}

export function gradeBooks(grade) {
  const books = [];
  for (const book of ["上", "下"]) {
    const poems = poemsIn(grade, book);
    const pending = unverified().filter((u) => u.grade === grade && u.book === book);
    if (poems.length || pending.length) books.push({ book, poems, pending });
  }
  return books;
}
