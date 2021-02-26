function array6(nums: number[], i: number): boolean {
  return array6Helper(nums, i, false);
}
function array6Helper(nums: number[], i: number, hasSix: boolean): boolean {
  if (i >= nums.length) return hasSix;
  if (nums[i] === 6) hasSix = true;
  return array6Helper(nums, ++i, hasSix);
}