function frontTimes(str: string, n: number): string {
  let extractedStr: string = '';
  if (str.length < 3) {
    extractedStr = str;
  } else {
    extractedStr = str.substr(0, 3);
  }
  return frontTimesHelper(extractedStr, n);
}

function frontTimesHelper (extractedStr: string, n: number): string {
  if (n === 0) return '';
  return extractedStr + frontTimesHelper(extractedStr, --n);
}