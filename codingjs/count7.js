function count7(n: number): number{
  if (n < 10) {
    return n === 7 ? 1 : 0;
  }
  return count7Helper(n, 0);
}
function count7Helper(dividend: number, count: number): number {
  if (dividend < 10) {
    return dividend === 7 ? count + 1 : count;
  }
  count = dividend % 10 === 7 ? count + 1 : count;
  return count7Helper(Math.floor(dividend / 10), count);
}