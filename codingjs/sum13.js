function sum13(nums: number[]): number{
  return sum13Helper(nums, 0);
}

function sum13Helper(nums: number[], index: number): number {
  if (nums.length === 0) return 0;
  if (nums.length <= index) return 0;
  if (nums[index] === 13) return 0 + sum13Helper(nums, index + 2);
  return nums[index] + sum13Helper(nums, ++index)
}