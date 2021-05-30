boolean doubleX(String str) {
  //solution 1
  // for (int i = 0; i < str.length() - 1; i++) {
  //   if (str.charAt(i) == 'x') return str.charAt(i + 1) == 'x'; 
  // }
  // return false;
  
  //solution 2
  // int firstXPos = str.indexOf("x");
  // if (firstXPos == str.length() - 1 || firstXPos == -1) return false;
  // return str.substring(firstXPos, firstXPos + 2).equals("xx");
  
  //solution 3
  int firstXPos = str.indexOf("x");
  if (firstXPos == str.length() - 1 || firstXPos == -1) return false;
  return str.substring(firstXPos).startsWith("xx");
}

