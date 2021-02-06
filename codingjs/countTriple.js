function countTriple(str: string): number {
  if (str.length < 3) return 0;
  return countTripleHelper(str, 0);
}
function countTripleHelper(str: string, count: number): number {
  if (str.length < 3) return count;
  if (str.substr(0, 1) == str.substr(1, 1) && str.substr(1, 1) == str.substr(2, 1)) {
    count++;
  }
  return countTripleHelper(str.substring(1), count);
}