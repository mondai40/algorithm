public int arrayCount9(int[] nums) {
  int nineCount = 0;
  for (int num: nums) {
    if (num == 9) nineCount++;
  }
  return nineCount;
}

