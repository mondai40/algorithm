function bigDiff(nums: number[]): number {
  return bigDiffHelper(nums, nums[0], nums[0], 0);
}

function bigDiffHelper(nums: number[], maxNum: number, minNum: number, index: number): number {
  if (index >= nums.length) return maxNum - minNum;
  return bigDiffHelper(nums, compMaxNum(maxNum, nums[index]), compMinNum(minNum, nums[index]), ++index)
}

function compMaxNum(presentNum: number, compNum: number): number {
  if (presentNum > compNum) return presentNum;
  return compNum;
}
function compMinNum(presentNum: number, compNum: number): number {
  if (presentNum < compNum) return presentNum;
  return compNum;
}