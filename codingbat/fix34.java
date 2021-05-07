public int[] fix34(int[] nums) {
  int[] result = nums.clone();
  for (int i = 0; i < result.length; i++) {
    if (result[i] == 3) {
      for (int j = 0; j < nums.length; j++) {
        if (result[j] == 4 && result[j - 1] != 3) {
          int temp = result[i + 1];
          result[i + 1] = 4;
          result[j] = temp;
        }
      }
    }
  }
  return result;
}

