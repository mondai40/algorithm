function maxEnd3(nums: number[]): number[] {
  const largerOnSide = nums[0] > nums[nums.length - 1] ? nums[0] : nums[nums.length - 1];
  return new Array(3).fill(largerOnSide);
}
