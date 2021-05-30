public int countYZ(String str) {
  int count = 0;
  for (int i = 0; i < str.length(); i++) {
    char target = Character.toLowerCase(str.charAt(i));
    if ((i == str.length() - 1) && (target == 'y' || target == 'z')) {
      count++;
      continue;
    } 
    if ((target == 'y' || target == 'z') && !Character.isLetter(str.charAt(i + 1))) {
      count++;
    }
  }
  return count;
}

