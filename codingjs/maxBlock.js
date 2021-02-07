function maxBlock(str: string): number {
  if (str.length === 0) return 0;
  if (str.length === 1) return 1;
  return maxBlockHelper(str.substr(1), str.substr(0, 1), 1, 0);
}
function maxBlockHelper(str: string, prevChar: string, count: number, maxCount: number): number {
  if (str === "") {
    return count > maxCount ? count : maxCount;
  }
  if (str.substr(0, 1) === prevChar) {
    count++;
  } else {
    maxCount = count > maxCount ? count : maxCount;
    count = 1;
  }
  prevChar = str.substr(0, 1)
  return maxBlockHelper(str.substr(1), prevChar, count, maxCount);
}