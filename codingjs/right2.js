function right2(str: string): string {
  const strLen: number = str.length;
  return str.substring(strLen - 2) + str.substring(0, strLen - 2);
}