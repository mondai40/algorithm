function only14(nums){
  return only14Helper(nums);
}

function only14Helper(nums) {
  if (nums.length === 0) return true;
  if (nums[0] === 1 || nums[0] === 4) {
    return only14Helper(nums.slice(1));
  } else {
    return false;
  }
  
}