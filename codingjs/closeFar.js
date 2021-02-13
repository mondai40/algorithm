function closeFar(a: number, b: number, c: number): boolean {
  if (Math.abs(a - b) <= 1 && Math.abs(a - c) <= 1) return false;
  if (Math.abs(a - b) <= 1 || Math.abs(a - c) <= 1) {
    return Math.abs(b - c) >= 2;
  }
}