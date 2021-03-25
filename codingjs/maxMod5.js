function maxMod5(a: number, b: number): number {
  if (a === b) return 0;
  if (a % 5 === b % 5) return a < b ? a : b;
  return a > b ? a : b;