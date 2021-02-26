function noX(str: string): string{
  return noXHelper(str, '');
}
function noXHelper(str: string, result: string): string {
  if (str.length === 0) return result;
  if (str.substr(0, 1) != "x") {
    result += str.substr(0, 1);
  }
  return noXHelper(str.substring(1), result);
}