function sum2(nums: number[]): number {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];
  if (nums.length >= 2) return nums[0] + nums[1];
}