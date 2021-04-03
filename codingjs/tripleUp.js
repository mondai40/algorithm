function tripleUp(nums){
  if (nums.length < 3) return false;
  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] === nums[i + 1] - 1 && nums[i] === nums[i + 2] - 2) {
      return true;
    }
  }
  return false;
}