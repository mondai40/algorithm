public List<String> lower(List<String> strings) {
  // with lamda
  // strings.replaceAll(n -> n.toLowerCase());
  // return strings;
  
  // with stream
  List<String> newStrs = new ArrayList<String>();
  newStrs = strings.stream()
    .map(n -> n.toLowerCase())
    .collect(Collectors.toList());
  return newStrs;
}

