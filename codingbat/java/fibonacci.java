public int fibonacciHelper(int n, int s1, int s2) {
  if (n == 0) return s1;
  return fibonacciHelper(--n, s2, s1 + s2);
}

public int fibonacci(int n) {
  return fibonacciHelper(n, 0, 1);
}

