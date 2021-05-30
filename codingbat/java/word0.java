public Map<String, Integer> word0(String[] strings) {
  Map<String, Integer> result = new HashMap<String, Integer>();
  for (String target: strings) {
    if (result.containsKey(target)) continue;
    result.put(target, 0);
  }
  return result;
}

