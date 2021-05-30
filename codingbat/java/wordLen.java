public Map<String, Integer> wordLen(String[] strings) {
  Map<String, Integer> map = new HashMap<String, Integer>();
  for (String target: strings) {
    if (map.containsKey(target)) continue;
    map.put(target, target.length());
  }
  return map;
}

