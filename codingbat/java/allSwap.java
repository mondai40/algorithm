public String[] allSwap(String[] strings) {
  Map<Character, Integer>charMap = new HashMap<Character, Integer>();
  String[] result = new String[strings.length];
  for (int i = 0; i < strings.length; i++) {
    char firstChar = strings[i].charAt(0);
    if (charMap.containsKey(firstChar)) {
      // swapped position
      int newPos = charMap.get(firstChar);
      // the present value
      String tempStr = strings[newPos];
      // swap
      result[newPos] = strings[i];
      result[i] = tempStr;
      // remove the used position
      charMap.remove(firstChar);
    } else {
      charMap.put(firstChar, i);
      result[i] = strings[i];
    }
  }
  return result;
}

