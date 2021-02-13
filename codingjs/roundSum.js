function roundSum(a: number, b: number, c: number): number{
  return roundSumHelper(Array.from(arguments), 0);
}
function roundSumHelper(nums: number[], result: number): number {
  if (nums.length === 0) return result;
  result += Math.round(nums[0] / 10) * 10;
  return roundSumHelper(nums.slice(1), result);
}