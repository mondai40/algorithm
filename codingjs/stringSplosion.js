function stringSplosion(str: string): string{
     return stringSplosionHelper(str, 0);
}
function stringSplosionHelper(str: string, n: number): string {
  if (str.length - 1 === n) return str;
  return str.substr(0, n + 1) + stringSplosionHelper(str, ++n);
}