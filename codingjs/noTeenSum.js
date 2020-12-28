function noTeenSum(a: number, b: number, c: number): number {
  return noTeenSumHelper(Array.from(arguments));
}
function noTeenSumHelper(numArr: number[]): number {
  if (numArr.length === 0) return 0;
  if (/^1[3, 4, 7, 8, 9]$/.test(numArr[0])) {
    return 0 + noTeenSumHelper(numArr.splice(1));
  }
  return numArr[0] + noTeenSumHelper(numArr.splice(1));
}