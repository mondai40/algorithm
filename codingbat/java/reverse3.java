public int[] reverse3(int[] nums) {
  int[] reversedNums = new int[nums.length];
  for (int i = nums.length - 1; i >= 0; i--) {
    reversedNums[(nums.length - 1) - i] = nums[i];
  }
  return reversedNums;
}

