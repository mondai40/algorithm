function twoTwo(nums: number[]): boolean {
  if (nums.indexOf(2) === -1) return true;
  return twoTwoHelper(nums, 1, false):
}
function twoTwoHelper(nums: number[], index: number, result: boolean): boolean {
  if (index >= nums.length) return result;
  if (nums[index] === 2) {
    if (nums[index - 1] === 2) {
      result = true;
    } else {
      result = false;
    }
  }
  return twoTwoHelper(nums, ++index, result):
}