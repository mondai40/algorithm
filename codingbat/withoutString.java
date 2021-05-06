public String withoutString(String base, String remove) {
  String result = "";
  String lowerBase = base.toLowerCase();
  String lowerRemove = remove.toLowerCase();
  int i = 0;
  while (i < base.length()) {
    if ((i <= base.length() - remove.length()) && lowerBase.substring(i, i + remove.length()).equals(lowerRemove)) {
      i += remove.length();
    } else {
      result += base.charAt(i);
      i++;
    }
  }
  return result;
}

