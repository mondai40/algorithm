function zipZap(str: string): string {
  if (str.length < 3) return str;
  let result = "";
  let i = 0;
  while (i < str.length) {
    if (str[i] === "z" && str[i + 2] === "p") {
      result += "zp";
      i += 3;
    } else {
      result += str[i];
      i++;
    }
  }
  return result;
}