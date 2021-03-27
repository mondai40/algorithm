function sumLimit(a: number, b: number): number {
  const sum = a + b;
  if (a.toString().length === sum.toString().length) return sum;
  else if (a.toString().length < sum.toString().length) return a;
}