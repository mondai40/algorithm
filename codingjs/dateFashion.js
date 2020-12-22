function dateFashion(you: number, date: number): number {
  if (you <= 2 || date <= 2) return 0;
  if (you >= 8 || date >= 8) return 2;
  return 1;
}