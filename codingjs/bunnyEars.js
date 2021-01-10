function bunnyEars(bunnies: number): number {
  return bunnyEarsHelper(bunnies, 0);
}
function bunnyEarsHelper(bunnies: number, result: number): number {
  if (bunnies === 0) return result;
  return bunnyEarsHelper(--bunnies, result + 2);
}