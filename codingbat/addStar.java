public List<String> addStar(List<String> strings) {
  List<String> result = new ArrayList<String>(strings.size());
  for (String word: strings) {
    result.add(word + "*");
  }
  return result;
}

