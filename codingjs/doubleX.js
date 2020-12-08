function doubleX(str: string): boolean{
  if (str.length < 2) return false;
  if (str[0] === 'x') {
    return str[1] === 'x';
  } else {
    return doubleX(str.substr(1));
  }
}