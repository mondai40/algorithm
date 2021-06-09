public boolean endOther(String a, String b) {
  int i = 0;
  String lowA = a.toLowerCase();
  String lowB = b.toLowerCase();
  while (lowA.substring(i).length() >= lowB.length()) {
    if (lowA.substring(i).equals(lowB)) return true;
    i++;
  }
  int j = 0;
  while (lowA.length() <= lowB.substring(j).length()) {
    if (lowB.substring(j).equals(lowA)) return true;
    j++;
  }
  return false;
}

