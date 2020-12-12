function firstTwo(str: string): string{
  if (str.length < 3) return str;
  return str.substring(0, 2);
}