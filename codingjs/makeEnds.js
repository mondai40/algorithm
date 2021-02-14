function makeEnds(nums: number[]): number[]{
  if (nums.length === 1) return [nums[0], nums[0]]
  if (nums.length === 2) return nums;
  return [nums[0], nums[nums.length - 1]];
}