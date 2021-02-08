function old35(n: number): boolean {
  if (n % 15 === 0) return false;
  return n % 3 === 0 || n % 5 === 0;
}