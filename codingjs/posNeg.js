function posNeg(a: numbr, b: number, negative: boolean): boolean{
  if (negative) return a < 0 && b < 0;
  return (a > 0 && b < 0) || (a < 0 && b > 0)
}