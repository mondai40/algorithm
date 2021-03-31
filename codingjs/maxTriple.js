function maxTriple(nums){
  if (nums.length === 1) return nums[0];
  const middlePos = Math.floor(nums.length / 2);
  return Math.max(nums[0], nums[middlePos], nums[nums.length - 1]);
}