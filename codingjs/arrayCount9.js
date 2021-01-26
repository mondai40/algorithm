function arrayCount9(nums: number[]): number {
  return arrayCount9Helper(nums, 0);
}
function arrayCount9Helper(nums: number[], count: number): number {
  if (nums.length === 0) return count;
  if (nums[0] === 9) count++;
  return arrayCount9Helper(nums.slice(1), count);
}