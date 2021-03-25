function redTicket(a: number, b: number, c: number): number {
  if (a === 2 && a === b && a === c) return 10;
  if (a === b && a === c) return 5;
  if (a !== b && a !== c) return 1;
  return 0;
}