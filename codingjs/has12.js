function has12(nums: number[]): boolean {
  const onePos = nums.indexOf(1);
  if (onePos === -1) return false;
  for (let i = onePos + 1; i < nums.length; i++) {
    if (nums[i] === 2) return true
  }
  return false;
}