function twoChar(str: string, index: number): string {
  if (str.length < 2) return str;
  if (index > str.length - 2 || index < 0) return str.substring(0, 2);
  return str.substr(index, 2);
}