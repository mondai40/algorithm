function swapEnds(nums){
  if (nums.length === 1) return nums;
  return [nums[nums.length - 1], ...nums.splice(1, nums.length - 2), nums[0]]
}