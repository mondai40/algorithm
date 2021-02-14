function has23(nums: number[]): boolean{
  const numArr = Array.from(arguments)
  return has23Helper(nums);
}
function has23Helper(nums: number[]): boolean {
  if (nums.length === 0) return false;
  if (nums[0] === 2 || nums[0] === 3) return true;
  return has23Helper(nums.slice(1));
} 