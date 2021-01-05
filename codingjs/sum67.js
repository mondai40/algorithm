function sum67(nums: number[]): number{
  return sum67Helper(nums, 0, false);
}
function sum67Helper(nums: number[], index: number, flag: boolean): number {
  if (nums.length <= index) return 0;
  
  if (nums[index] === 6 && !flag) flag = true;
  if (nums[index] === 7 && flag) return 0 + sum67Helper(nums, ++index, false);
  
  if (flag) return 0 + sum67Helper(nums, ++index, flag);
  return nums[index] + sum67Helper(nums, ++index, false);
}