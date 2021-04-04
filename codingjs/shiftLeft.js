function shiftLeft(nums){
  if (nums.length <= 1) return nums;
  return [...nums.slice(1), nums[0]];
}