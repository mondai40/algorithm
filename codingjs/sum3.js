function sum3(nums: number[]): number { 
  if (nums.length < 2) return nums[0];
  return nums[0] + sum3(nums.splice(1));
}