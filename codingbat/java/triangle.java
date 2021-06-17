public int triangleHelper(int rows, int sumBlocks) {
  if (rows == 0) return sumBlocks;
  sumBlocks += rows;
  return triangleHelper(--rows, sumBlocks);
}

public int triangle(int rows) {
  return triangleHelper(rows, 0);
}

