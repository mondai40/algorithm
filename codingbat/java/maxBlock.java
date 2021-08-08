public int maxBlock(String str) {
  int count = 0;
  int maxCount = 0;
  if (str.length() <= 1) return str.length();
  
  char prevChar = str.charAt(0);
  for (int i = 0; i < str.length(); i++) {
    if (prevChar == str.charAt(i)) {
      count++;
      maxCount = count > maxCount ? count : maxCount;
    } else {
      maxCount = count > maxCount ? count : maxCount;
      count = 1;
    }
    prevChar = str.charAt(i);
  }
  return maxCount;
}

