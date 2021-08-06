public int sum2(int[] nums) {
  int end = nums.length < 2 ? nums.length : 2;
  int total = 0;
  for (int i = 0; i < end; i++) {
    total += nums[i];
  }
  return total;
}

