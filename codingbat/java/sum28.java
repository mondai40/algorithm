public boolean sum28(int[] nums) {
  int totalOfTwo = 0;
  for (int num: nums) {
    if (num == 2) totalOfTwo += 2;
  }
  return totalOfTwo == 8;
}

