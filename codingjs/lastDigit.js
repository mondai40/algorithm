function lastDigit(a: number, b: number): boolean {
  const devider = 10;
  return a % devider === b % devider;
}