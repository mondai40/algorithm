function triangle(rows: number): number {
  return triangleHelper(rows, 0);
}

function triangleHelper(rows: number, result: number): number {
  if (rows === 0) return result;
  result += rows
  return triangleHelper(--rows, result)
}