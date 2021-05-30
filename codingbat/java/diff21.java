public int diff21(int n) {
  int target = 21;
  return n > 21 ? Math.abs(target - n) * 2 : Math.abs(target - n);
}

