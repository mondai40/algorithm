function twoAsOne(a: number, b: number, c: number): boolean {
  if (a + b === c) return true;
  if (a + c === b) return true;
  if (b + c === a) return true;
  return false;
}