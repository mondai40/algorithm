public int countClumps(int[] nums) {
  if (nums.length < 2) return 0;
  int count = 0;
  int prevNum = nums[0];
  int clumpsCount = 0;
  for (int num: nums) {
    if (num == prevNum) {
      count++;
    } else {
      if (count >= 2) clumpsCount++;
      count = 1;
    }
    prevNum = num;
  }
  if (count >= 2) clumpsCount++;
  return clumpsCount;
}

