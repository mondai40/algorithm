public Map<String, String> firstChar(String[] strings) {
  Map<String, String> result = new HashMap<>();
  for (String word: strings) {
    String firstChar = word.substring(0, 1);
    if (result.containsKey(firstChar)) {
      result.put(firstChar, result.get(firstChar) + word);
    } else {
      result.put(firstChar, word);
    }
  }
  return result;
}

