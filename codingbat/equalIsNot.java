public boolean equalIsNot(String str) {
  int isCount = 0;
  int notCount = 0;
  for (int i = 0; i < str.length() - 1; i++) {
    if (str.substring(i).startsWith("is")) isCount++;
    if (i < str.length() - 1 && str.substring(i).startsWith("not")) notCount++;
  }
  return isCount == notCount;
}

