public int roundSum(int a, int b, int c) {
  return round10(a) + round10(b) + round10(c);
}

public int round10(double num) {
  return (int)(Math.round(num / 10) * 10);
}

