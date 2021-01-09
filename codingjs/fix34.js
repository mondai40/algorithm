function fix34(nums: number[]): number[] {
  if (nums.length <= 0) return nums;
  const threeFourArray = getThreeFourArray(nums, 0, []);
//   return threeFourArray;
  return fix34Helper(nums, 0, threeFourArray);
}
function fix34Helper(nums: number[], index: number, result) {
  if (index >= nums.length) return result;
  if (nums[index] !== 3 && nums[index] !== 4) {
    result[result.indexOf(undefined)] = nums[index];
  }
  return fix34Helper(nums, ++index, result)
}
function getThreeFourArray(nums: number[], index: number, result: number[]): number[] {
  if (index >= nums.length) return result;
  if (nums[index] === 3) {
    result[index] = 3;
    result[index + 1] = 4;
    return getThreeFourArray(nums, index + 2, result)
  }
  result[index] = undefined;
  return getThreeFourArray(nums, ++index, result);
}