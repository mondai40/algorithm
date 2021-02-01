function middleThree(str: string): string {
  if (str.length < 4) return str;
  const startPos = Math.floor(str.length / 2) - 1;
  return str.substr(startPos, 3);
}