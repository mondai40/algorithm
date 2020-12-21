function equalIsNot(str: string): boolean {
  const isNum = str.match(/is/g) ? str.match(/is/g).length : 0;
  const notNum = str.match(/not/g) ? str.match(/not/g).length : 0;
  return isNum === notNum;
}