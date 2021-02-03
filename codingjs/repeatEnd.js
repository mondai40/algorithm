function repeatEnd(str: string, n: number): string {
//   return str.substring(str.length - n).repeat(n);
  return repeatEndHelper(str.substring(str.length - n), n, "");
}
function repeatEndHelper(target: string, count: index, result: string): string {
  if (count === 0) return result;
  result += target
  return repeatEndHelper(target, --count, result);
}