public boolean xyzThere(String str) {
  String target = "xyz";
  for (int i = 0; i <= str.length() - target.length(); i++) {
    if (str.substring(i, i + target.length()).equals(target)) {
      if (i == 0) return true;
      else if (str.charAt(i - 1) != '.') return true;
    }
  }
  return false;
}

