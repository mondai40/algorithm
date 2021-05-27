public Map<String, Integer> wordCount(String[] strings) {
  Map<String, Integer> result = new HashMap<String, Integer>();
  for (String alphabet: strings) {
    if (result.containsKey(alphabet)) {
      result.put(alphabet, result.get(alphabet) + 1);
    } else {
      result.put(alphabet, 1);
    }
  }
  return result;
}

