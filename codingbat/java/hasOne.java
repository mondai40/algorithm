public boolean hasOne(int n) {
  return hasOneHelper(n);
}

public boolean hasOneHelper(int n) {
  // base case
  if (n < 10) return n == 1;
  
  if (n % 10 == 1) return true;
  n /= 10;
  return hasOneHelper(n);
}
