function lastChars(a: string, b: string): string {
  let result = "";
  if (a.length === 0) {
    result += "@";
  } else {
    result += a.substr(0, 1)
  }
  if (b.length === 0) {
    result += "@";
  } else {
    result += b.substr(b.length - 1, 1)
  }
  return result;
}