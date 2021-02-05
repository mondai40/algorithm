function xyzMiddle(str: string): boolean {
  if (str.length < 3) return false;
  return xyzMiddleHelper(str, 0);
}
function xyzMiddleHelper(str: string, n: index): boolean {
  if (str.substring(n).length < 3) return false;
  if (str.substr(n, 3) === "xyz") {
    if Math.abs(n - str.substring(n + 3).length) <= 1 {
      return true;
    }
  }
  return xyzMiddleHelper(str, ++n);
}