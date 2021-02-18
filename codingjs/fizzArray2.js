function fizzArray2(n: number): string {
  if (n === 0) return [];
  const result = [];
  for (let i = 0; i < n; i++) {
    result.push(String(i))
  }
  return result;
}