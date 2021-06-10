public int sum67(int[] nums) {
  boolean stopSum = false;
  int total = 0;
  for (int num: nums) {
    if (num == 6) stopSum = true;
    if (!stopSum) total += num;
    if (num == 7) stopSum = false;
  }
  return total;
}

