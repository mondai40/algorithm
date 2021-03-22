function wordEnds(str: string, word: string): string {
  if (str.length <= word.length) return "";
  let result = "";
  for (let i = 0; i <= str.length - word.length; i++) {
    if (i === 0 && str.substr(i, word.length) === word) {
      result += str[i + word.length];
    } else if (i === str.length - word.length && str.substr(i, word.length) === word) {
      result += str[i - 1];
    } else if (str.substr(i, word.length) === word) {
      result += str[i - 1] + str[i + word.length];
    }
  }
  return result;
}