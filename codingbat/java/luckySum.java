public int luckySum(int a, int b, int c) {
  // the question is tricky.
  // if you got 13, you just stop sum.
  if (a == 13) return 0;
  if (b == 13) return a;
  if (c == 13) return a + b;
  return a + b + c;
}

