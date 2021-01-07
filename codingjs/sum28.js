function sum28(nums: number[]): boolean{
  return sum28Helper(nums, 0, 0);
}
function sum28Helper(nums: number[], twoSum, index): boolean {
  if (index >= nums.length) return twoSum === 8;
  if (nums[index] === 2) {
    return sum28Helper(nums, twoSum + 2, ++index);
  }
  return sum28Helper(nums, twoSum, ++index);
}