function prependSum(nums: number[]): number[]{
  return prependSumHelper(nums, 0, [])
}
function prependSumHelper(nums: number[], index: number, result: number[]): number[] {
  if (index >= nums.length) return result;
  
  if (index >= 2) {
    result.push(nums[index])
    return prependSumHelper(nums, ++index, result);
  } else {
    result.push(nums[0] + nums[1])
    return prependSumHelper(nums, 2, result);
  }
}