function midThree(nums){
  if (nums.length < 4) return nums;
  const startPos = Math.floor(nums.length / 2) - 1;
  return [nums[startPos], nums[startPos + 1], nums[startPos + 2]];
}