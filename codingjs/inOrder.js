function inOrder(a: number, b: number, c: number, bOk: boolean): boolean {
  if (bOk) {
    return b < c;
  } else {
    return b > a && b < c;
  }
}