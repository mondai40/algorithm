public boolean closeFar(int a, int b, int c) {
  if (Math.abs(a - b) <= 1) {
    return Math.abs(c - a) >= 2 && Math.abs(c - b) >= 2;
  }
  if (Math.abs(a - c) <= 1) {
    return Math.abs(b - a) >= 2 && Math.abs(b - c) >= 2;
  }
  return false;
}

