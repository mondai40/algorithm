function notReplace(str: string): string {
  let result = '';
  let customStr = ' ' + str + ' ';
  for (let i = 1; i < customStr.length - 1; i++) {
    if (customStr.substr(i, 2) === 'is' && /[^a-zA-Z]/.test(customStr[i - 1]) && /[^a-zA-Z]/.test(customStr[i + 2])) {
      result += 'is not';
      i++;
    } else {
      result += customStr[i];
    }
  }
  return result;
}