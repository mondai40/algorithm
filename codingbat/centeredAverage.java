public int centeredAverage(int[] nums) {
  int minNum = nums[0];
  int maxNum = nums[0];
  int sumNum = 0;
  for (int num: nums) {
    if (minNum > num) minNum = num;
    if (maxNum < num) maxNum = num;
    sumNum += num;
  }
  sumNum -= (minNum + maxNum);
  return sumNum / (nums.length - 2);
}

