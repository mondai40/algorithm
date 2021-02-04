function repeatFront(str: string, n: number): string {
  if (str === "" || n === 0) return "";
  const target = str.substring(0, n);
  return repeatFrontHelper(target, n, "");
}
function repeatFrontHelper(str, count, result) {
  if (count === 0) return result;
  result += str;
  count--;
  const newTarget = str.substring(0, str.length - 1)
  return repeatFrontHelper(newTarget, count, result);
}