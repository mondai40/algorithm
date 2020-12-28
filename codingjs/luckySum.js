function luckySum(a: number, b: number, c: number): number{
  // [...arguments] won't work because of javascript version?
  return luckySumHelper(Array.from(arguments));
}

function luckySumHelper(numArr) {
  if (numArr.length === 0 || numArr[0] === 13) return 0;
  return numArr[0] + luckySumHelper(numArr.splice(1));
}