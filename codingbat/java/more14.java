public boolean more14(int[] nums) {
  int oneCount = 0;
  int fourCount = 0;
  for (int num: nums) {
    if (num == 1) oneCount++;
    if (num == 4) fourCount++;
  }
  return oneCount > fourCount;
}

