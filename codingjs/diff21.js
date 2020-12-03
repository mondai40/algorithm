function diff21(n: number): number{
  if (n <= 21) return Math.abs(n - 21);
  return Math.abs(n - 21) * 2;
}