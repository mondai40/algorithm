function conCat(a: string, b: string): string{
  const isDoubleChar = a.substring(a.length - 1) === b[0];
  if (isDoubleChar) return a + b.substring(1);
  return a + b;
}