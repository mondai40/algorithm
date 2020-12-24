function sortaSum(a: number, b: number): number {
  const sum: number = a + b;
  return (sum >= 10 && sum <= 19) ? 20 : sum;
}