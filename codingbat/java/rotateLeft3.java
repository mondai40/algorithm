public int[] rotateLeft3(int[] nums) {
  int[] result = new int[nums.length];
  for (int i = 1; i < nums.length; i++) {
    result[i - 1] = nums[i];
  }
  result[result.length - 1] = nums[0];
  return result;
}

