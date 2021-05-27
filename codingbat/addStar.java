public List<String> addStar(List<String> strings) {
  // List<String> result = new ArrayList<String>(strings.size());
  // for (String word: strings) {
  //   result.add(word + "*");
  // }
  // return result;
  
  //with lamda
  // strings.replaceAll(n -> n + "*");
  // return strings;
  
  //with lamda and stream
  List<String> result = new ArrayList<String>(strings.size());
  result = strings.stream()
    .map(n -> n + "*")
    .collect(Collectors.toList());
  
  return result;
}

