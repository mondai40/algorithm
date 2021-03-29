function makeMiddle(nums){
  if (nums.length < 3) return nums;
  const startPos = Math.ceil(nums.length / 2) - 1;
  return [nums[startPos], nums[startPos + 1]];
}