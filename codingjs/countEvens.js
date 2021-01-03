function countEvens(nums: number[]): number {
  return countEvensHelper(nums, 0)
}
function countEvensHelper(nums: number[], count: number): number {
  if (nums.length === 0) return count;
  if (nums[0] % 2 === 0) return countEvensHelper(nums.splice(1), ++count);
  return countEvensHelper(nums.splice(1), count)
}