function notAlone(nums, val){
  if (nums.length < 3) return nums;
  for (let i = 1; i < nums.length - 1; i++) {
    if (nums[i] === val && nums[i - 1] != val && nums[i + 1] != val) {
      nums[i] = nums[i - 1] > nums[i + 1] ? nums[i - 1] : nums[i + 1];
    }
  }
  return nums;
}