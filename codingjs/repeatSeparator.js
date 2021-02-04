function repeatSeparator(word: string, sep: string, count: number): number {
  if (count === 0) return "";
  return repeatSeparatorHelper(word, sep, count, "");
}
function repeatSeparatorHelper(word: string, sep: string, count: number, result: string): string {
  if (count === 1) return result + word;
  result += word + sep
  count--;
  return repeatSeparatorHelper(word, sep, count, result);
}