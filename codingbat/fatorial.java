public int factorialHelper(int n, int result) {
  if (n == 1) return result;
  result *= n;
  return factorialHelper(--n, result);
}

public int factorial(int n) {
  return factorialHelper(n, 1);
}

