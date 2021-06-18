public int sumDigitsHelper(int n, int sum) {
  if (n < 10) return sum + n;
  sum += n % 10;
  return sumDigitsHelper(n / 10, sum);
}

public int sumDigits(int n) {
  return sumDigitsHelper(n, 0);
}

