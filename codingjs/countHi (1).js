function countHi(str: string): number {
  return countHiHelper(str, 0);
}
function countHiHelper(str: string, count: number): number {
  if (str.length <= 1) return count;
  if (str.substr(0, 2) === "hi") {
    return countHiHelper(str.substring(2), ++count);
  } else {
    return countHiHelper(str.substring(1), count);
  }
}