function countHi(str: string): number {
  if (str.length < 3) return str === 'hi' ? 1 : 0;
  if (str.substring(0, 2) === 'hi') {
    return 1 + countHi(str.substring(2));
  } else {
    return 0 + countHi(str.substring(1));
  }
}