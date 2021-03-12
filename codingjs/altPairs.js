function altPairs(str: string): string {
  let i = 0;
  let result = "";
  while (i < str.length) {
    result += str[i];
    if (i % 2 === 0) {
      i++;
    } else {
      i += 3;
    }
  }
  return result;
}