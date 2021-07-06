public boolean xyBalance(String str) {
  // if I got 'x', add 1. If I got 'y', substract 1
  // if xyCount is 0 at the end, it is balanced
  int xyCount = 0;
  for (int i = 0; i < str.length(); i++) {
    if (str.charAt(i) == 'x' && xyCount > 0) continue;
    if (str.charAt(i) == 'y' && xyCount == 0) continue;
    if (str.charAt(i) == 'x') {
      xyCount++;
      continue;
    }
    if (str.charAt(i) == 'y') {
      xyCount--;
      continue;
    }
  }
  return xyCount == 0;
}

