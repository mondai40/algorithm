public String mirrorEnds(String string) {
  StringBuilder buf = new StringBuilder();
  
  for (int i = 0; i < string.length(); i++) {
    if (string.charAt(i) != string.charAt(string.length() - (i + 1))) break;
    buf.append(string.charAt(i));
  }
  
  return buf.toString();
}

