function isEverywhere(nums, val){
  return isEverywhereHelper(nums, val, 0);
}
function isEverywhereHelper(nums, val, index) {
  if (index >= nums.length - 1) return true;
  if (nums[index] != val && nums[index + 1] != val) {
    return false
  }
  return isEverywhereHelper(nums, val, ++index);
}