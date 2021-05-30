public int sum13(int[] nums) {
  if (nums.length < 1) return 0;
  int sumNum = 0;
  for (int i = 0; i < nums.length; i++) {
    if (nums[i] == 13) {
      i++;
      continue;
    }
    sumNum += nums[i];
  }
  return sumNum;
}

