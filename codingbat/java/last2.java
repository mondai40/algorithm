public int last2(String str) {
  if (str.length() <= 2) return 0;
  
  String target = str.substring(str.length() - 2);
  int targetCount = 0;
  for (int i = 0; i < str.length() - 2; i++) {
    if (str.substring(i, i + 2).equals(target)) targetCount++;
  }
  return targetCount;
}

