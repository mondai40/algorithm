function countCode(str: string): number{
  return str.match(/co.e/g) ? str.match(/co.e/g).length : 0;
}