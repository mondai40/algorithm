public Map<String, String> pairs(String[] strings) {
  Map<String, String> result = new HashMap<String, String>();
  
  for (String string: strings) {
    result.put(string.substring(0, 1), string.substring(string.length() - 1));
  }
  return result;
}

