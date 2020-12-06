function stringTimes(str: string, n: number): string{
  if (n === 0) return '';
  return str + stringTimes(str, --n);
}