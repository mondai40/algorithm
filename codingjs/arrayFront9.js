function arrayFront9(nums: number[]): boolean {
  return arrayFront9Helper(nums, 0);
}
function arrayFront9Helper(nums: number[], index: number): boolean {
  if (index > 3) return false;
  return nums[index] === 9 ? true : arrayFront9Helper(nums, ++index);
} 