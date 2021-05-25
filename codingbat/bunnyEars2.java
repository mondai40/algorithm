public int bunnyEars2Helper(int bunnies, int ears) {
  if (bunnies == 0) return ears;
  if (bunnies % 2 == 0) return bunnyEars2Helper(--bunnies, ears + 3);
  return bunnyEars2Helper(--bunnies, ears + 2);
}

public int bunnyEars2(int bunnies) {
  return bunnyEars2Helper(bunnies, 0);
}

