function xyBalance(str: string): boolean {
  const xLastPos = str.lastIndexOf('x');
  const yLastPos = str.lastIndexOf('y');
  return xLastPos <= yLastPos;
}