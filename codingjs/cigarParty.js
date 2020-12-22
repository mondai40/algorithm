function cigarParty(cigars: number, isWeekend: boolean): boolean {
  if (isWeekend) return cigars >= 40;
  return cigars >= 40 && cigars <= 60;
}