function stringX(str: string): string {
  if (str.length < 1) return "";
  const firstChar = str.substr(0, 1);
  const lastChar = str.substr(str.length - 1, 1);
  const middleStr = str.substring(1, str.length - 1).replace(/x/g, "");
  return firstChar + middleStr + lastChar;
}