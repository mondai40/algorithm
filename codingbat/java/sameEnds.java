public String sameEnds(String string) {
  int firstEnd = string.length() / 2;
  int secondStart = (int)Math.ceil((double)string.length() / 2);
  for (int i = 0; i <= firstEnd; i++) {
    if (string.substring(0, firstEnd - i).equals(string.substring(secondStart + i))) {
      return string.substring(0, firstEnd - i);
    }
  }
  return "";
}

