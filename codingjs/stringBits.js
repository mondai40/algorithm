function stringBits(str: string): string{
  if (str.length === 0) return '';
  if (str.length <= 2) return str[0];
  return str[0] + stringBits(str.substr(2));
}