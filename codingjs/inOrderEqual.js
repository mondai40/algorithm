function inOrderEqual(a: number, b: number, c: number, equalOk: boolean): boolean {
  if (equalOk) {
    return (a <= b) && (b <= c);
  } else {
    return (a < b) && (b < c);
  }
}