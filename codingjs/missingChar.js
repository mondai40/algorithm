function missingChar(str: string, n: number): string{
  return str.substring(0, n) + str.substring(n + 1);
}