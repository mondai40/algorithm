public int count7Helper(int n, int count) {
  if (n < 10) return n == 7 ? count + 1 : count;
  int remainder = n % 10;
  count += remainder == 7 ? 1 : 0;
  int quotient = n / 10;
  return count7Helper(quotient, count);
}

public int count7(int n) {
  return count7Helper(n, 0);
}

