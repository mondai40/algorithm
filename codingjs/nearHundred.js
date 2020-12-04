function nearHundred(n: number): boolean{
  return Math.abs(n - 100) <= 10 || Math.abs(n - 200) <= 10;
}