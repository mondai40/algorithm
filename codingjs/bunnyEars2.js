function bunnyEars2(bunnies: number): number {
  if (bunnies <= 0) return 0;
  const numEars = bunnies % 2 == 1 ? 2 : 3;
  return numEars + bunnyEars2(--bunnies);
}