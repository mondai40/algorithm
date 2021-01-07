function lucky13(nums){
  return lucky13Helper(nums, 0);
}
function lucky13Helper(nums, index) {
  if (nums.length <= index) return true;
  if (nums[index] === 1 || nums[index] === 3) return false;
  return lucky13Helper(nums, ++index);
}
