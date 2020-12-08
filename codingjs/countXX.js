function countXX(str: string): number{
  if (str.length < 2) return 0;
  if (str.substr(0, 2) === 'xx') {
    return 1 + countXX(str.substr(1));
  } else {
    return 0 + countXX(str.substr(1));
  }
}