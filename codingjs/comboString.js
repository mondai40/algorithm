function comboString(a: string, b: string): string{
  if (a.length > b.length) return b + a + b;
  return a + b + a;
}