function last2(str: string): number {
  if (str.length <= 2) return 0;
  const word = str.substring(str.length - 2);
  return last2Helper(str, word, 0);
}
function last2Helper(target: string, word: string, count: number): number {
  if (target.length <= 0) return count - 1;
  if (target.substr(0, 2) === word) count++;
  return last2Helper(target.substring(1), word, count);
}