function count8(n: number): number {
  if (n < 8) return 0;
  return count8Helper(n, 0);
}

function count8Helper(n: number, count: number, isPrevEight: boolean): number {
  if (n === 0) return count;
  let eightCount = 0;
  if (n % 10 === 8) eightCount = 1;
  if (n % 100 === 88) eightCount = 2;
  return count8Helper(Math.floor(n / 10), count + eightCount);
}