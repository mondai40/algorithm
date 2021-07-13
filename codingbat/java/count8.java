public int count8Helper(int n, int count, boolean isPrevEight) {
  if (n < 10) {
    if (n == 8 && isPrevEight) return count + 2;
    else if (n == 8) return count + 1;
    else return count;
  }
  int remainder = n % 10;
  int quotient = n / 10;
  if (remainder == 8) {
    if (isPrevEight) count += 2;
    else count += 1;
    isPrevEight = true;
  } else {
    isPrevEight = false;
  }
  return count8Helper(quotient, count, isPrevEight);
}

public int count8(int n) {
  return count8Helper(n, 0, false);
}

