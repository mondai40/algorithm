public int countTriple(String str) {
  if (str.length() <= 2) return 0;
  
  int count = 0;
  for (int i = 0; i < str.length() - 2; i++) {
    if (str.charAt(i) == str.charAt(i + 1) && str.charAt(i) == str.charAt(i + 2)) {
      count++;
    }
  }
  return count;
}

