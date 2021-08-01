public String mixString(String a, String b) {
  int shortLen = Math.min(a.length(), b.length());
  String result = "";
  for (int i = 0; i < shortLen; i++) {
    result += a.charAt(i) + "" + b.charAt(i);
  }
  return result + a.substring(shortLen) + b.substring(shortLen);
}

