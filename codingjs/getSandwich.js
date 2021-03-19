function getSandwich(str: string): string {
  if (str.length < 10) return "";
  let startPos = 0;
  let endPos = 0;
  let i = 0;
  const bread = "bread";
  while (i < str.length) {
    if (str.substr(i, bread.length) === bread) {
      startPos = i + bread.length;
      break;
    }
    i++;
  }
  let j = str.length - 1;
  while (j >= 4) {
    if (str.substr(j, bread.length) === bread) {
      endPos = j;
      break;
    }
    j--;
  }
  return str.substring(startPos, endPos);
}