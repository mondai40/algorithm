public boolean canBalance(int[] nums) {
  if (nums.length < 2) return false;
  int leftSum = 0;
  for (int i = 0; i < nums.length - 1; i++) {
    leftSum += nums[i];
    int rightSum = 0;
    for (int j = i + 1; j < nums.length; j++) {
      rightSum += nums[j];
    }
    if (leftSum == rightSum) return true;
  }
  return false;
}

