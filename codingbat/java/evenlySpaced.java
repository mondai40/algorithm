public boolean evenlySpaced(int a, int b, int c) {
  if (a == b && b == c) return true;
  if (a == b || b == c || a == c) return false;
  
  int diffAB = Math.abs(a - b);
  int diffBC = Math.abs(b - c);
  int diffAC = Math.abs(a - c);
  if (diffAB == diffBC) return true;
  if (diffBC == diffAC) return true;
  if (diffAB == diffAC) return true;
  return false;
}

