function nTwice(str: string, n: number): string {
  if (str.length < n) return "";
  return str.substr(0, n) + str.substr(str.length - n);
}