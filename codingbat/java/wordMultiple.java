public Map<String, Boolean> wordMultiple(String[] strings) {
  Map<String, Boolean> result = new HashMap<>();
  for (String word: strings) {
    if (result.containsKey(word)) result.put(word, true);
    else result.put(word, false);
  }
  return result;
}

