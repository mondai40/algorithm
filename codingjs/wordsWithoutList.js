function wordsWithoutList(words: string[], len: number): string[] {
  return wordsWithoutListHelper(words, len, []);
}
function wordsWithoutListHelper(words: string[], len: number, result: string[]) {
  if (words[0] === undefined) return result;
  if (words[0].length === len) {
    return wordsWithoutListHelper(words.splice(1), len, result);
  } else {
    result.push(words[0]);
    return wordsWithoutListHelper(words.splice(1), len, result)
  }
}