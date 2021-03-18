function withoutX(str: string): string {
  if (str.length === 0) return "";
  if (str.length === 1) return str === "x" ? "" : str;
  const firstChar = str[0] === "x" ? "" : str[0];
  const lastChar = str[str.length - 1] === "x" ? "" : str[str.length - 1];
  return firstChar + str.substring(1, str.length - 1) + lastChar;
}