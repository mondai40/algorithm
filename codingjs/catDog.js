function catDog(str: string): boolean {
  const catNum: number = str.match(/cat/g) ? str.match(/cat/g).length : 0;
  const dogNum: number = str.match(/dog/g) ? str.match(/dog/g).length : 0;
  return catNum === dogNum;
}