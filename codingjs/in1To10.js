function in1To10(n: number, outsideMode: boolean): boolean {
  if (outsideMode) return n <= 1 || n >= 10;
  return n >= 1 && n <= 10;
}