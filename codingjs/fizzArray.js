function fizzArray(n: number): number[] {
  return fizzArrayHelper(n, []);
}
function fizzArrayHelper(n: number, result: number[]): number[] {
  if (n === 0) return result;
  result.unshift(n - 1);
  return fizzArrayHelper(--n, result);
}