public int bigDiff(int[] nums) {
  int minNum = nums[0];
  int maxNum = nums[0];
  for (int num: nums) {
    minNum = Math.min(num, minNum);
    maxNum = Math.max(num, maxNum);
  }
  return maxNum - minNum;
}

