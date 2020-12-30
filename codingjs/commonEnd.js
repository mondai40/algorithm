function commonEnd(a: number[], b: number[]): boolean {
  return a[0] === b[0] || a[a.length - 1] === b[b.length - 1];
}