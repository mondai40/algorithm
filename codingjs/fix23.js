function fix23(nums){
  return fix23Helper(nums, [], nums[0]):
}
function fix23Helper(nums, result, prevNum) {
  if (nums.length <= 0) return result;
  if (prevNum === 2 && nums[0] === 3) {
    result.push(0);
  } else {
    result.push(nums[0]);
  }
  return fix23Helper(nums.slice(1), result, nums[0]);
}