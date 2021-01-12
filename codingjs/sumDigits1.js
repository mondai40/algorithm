function sumDigits1(n: number): number {
  if (n < 10) return n;
  return sumDigits1Helper(n, 0);
}
function sumDigits1Helper(dividend: number, sum: number): number {
  if (dividend < 10) return dividend + sum;
  return sumDigits1Helper(Math.floor(dividend / 10), sum + (dividend % 10))
}