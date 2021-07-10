public int blackjack(int a, int b) {
  int fixedA = a > 21 ? 0 : a;
  int fixedB = b > 21 ? 0 : b;
  return Math.max(fixedA, fixedB);
}

