function prefixAgain(str: string, n: number): boolean {
  if (n === 0 || n >= str.length) return false;
  const target = str.substr(0, n)
  return prefixAgainHelper(str.substring(n), target, n);
}
function prefixAgainHelper(str, target, n) {
  if (str === "") return false;
  if (str.substr(0, n) === target) return true;
  return prefixAgainHelper(str.substring(1), target, n);
}