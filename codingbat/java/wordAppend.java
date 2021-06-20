public String wordAppend(String[] strings) {
  String result = "";
  
  Map<String, Integer> wordCountMap = new HashMap<>();
  for (String word: strings) {
    if (wordCountMap.containsKey(word)) {
      wordCountMap.put(word, wordCountMap.get(word) + 1);
      result += wordCountMap.get(word) % 2 == 0 ? word : "";
    } else {
      wordCountMap.put(word, 1);
    }
  }
  return result;
}

