function wordsCount(words: string[], len: number): number {
  return wordsCountHelper(words, len, 0, 0);
}
function wordsCountHelper(words: string[], len: number, index: number, count: number): number {
  if (index >= words.length) return count;
  if (words[index].length === len) count++;
  return wordsCountHelper(words, len, ++index, count);
}