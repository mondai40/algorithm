function plusOut(str: string, word: string): string {
  const spStep = word.length;
  let result = "";
  let i = 0;
  while (i < str.length) {
    if (str.substr(i, spStep) === word) {
      result += word;
      i += spStep;
      continue
    } else {
      result += "+";
      i++;
    }
  }
  return result;
}