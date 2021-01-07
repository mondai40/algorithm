function more14(nums: number[]): boolean {
  return more14Helper(nums, 0, 0, 0);
}
function more14Helper(nums: number[], oneCount: number, fourCount: number, index: number): boolean {
  if (index >= nums.length) return oneCount > fourCount;
  if (nums[index] === 1) return more14Helper(nums, ++oneCount, fourCount, ++index);
  if (nums[index] === 4) return more14Helper(nums, oneCount, ++fourCount, ++index);
  return more14Helper(nums, oneCount, fourCount, ++index);
}