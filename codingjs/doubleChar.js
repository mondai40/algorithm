function doubleChar(str: string): string {
  if (str.length < 2) return str.repeat(2);
  return str[0].repeat(2) + doubleChar(str.substring(1));
}