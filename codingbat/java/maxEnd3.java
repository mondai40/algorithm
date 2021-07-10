public int[] maxEnd3(int[] nums) {
  int maxNum = Math.max(nums[0], nums[2]);
  nums[0] = maxNum;
  nums[1] = maxNum;
  nums[2] = maxNum;
  return nums;
}

