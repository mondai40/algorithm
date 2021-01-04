function centeredAverage(nums: number[]): number {
  return centeredAverageHelper(nums, nums.indexOf(Math.max(...nums)), nums.indexOf(Math.min(...nums)), 0, 0, 0);
}
function centeredAverageHelper(nums: number[], maxNumIndex: number, minNumIndex: number, total: number, count: number, index: number): number {
  if (index >= nums.length) return total / count;
  if (maxNumIndex === index) return centeredAverageHelper(nums, maxNumIndex, minNumIndex, total, count, ++index)
  if (minNumIndex === index) return centeredAverageHelper(nums, maxNumIndex, minNumIndex, total, count, ++index)
  return centeredAverageHelper(nums, maxNumIndex, minNumIndex, total + nums[index], ++count, ++index)
}