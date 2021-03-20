function oneTwo(str: string): string {
  if (str.length < 3) return "";
  let result = "";
  let i = 0;
  while (str.substr(i, 3).length >= 3) {
    result += str.substr(i + 1, 2) + str.substr(i, 1);
    i += 3;
  }
  return result;
}