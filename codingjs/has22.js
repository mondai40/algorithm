function has22(nums){
  return has22Helper(nums, nums[0], 1);
}
function has22Helper(nums, prevNum, index) {
  if (nums.length <= index) return false;
  if (nums[index] === prevNum) return true;
  return has22Helper(nums, nums[index], ++index);
}