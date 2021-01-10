function fibonacci(n: number): number {
  return fibonacciHelper(0, 1, n);
}
function fibonacciHelper(f1: number, f2: number, n: number): number {
  if (n === 0) return f1;
  return fibonacciHelper(f2, f1 + f2, --n);
}