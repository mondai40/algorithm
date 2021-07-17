public List<String> noYY(List<String> strings) {
  // List<String> result = new ArrayList<>();
  // for (int i = 0; i < strings.size(); i++) {
  //   if ((strings.get(i) + "y").indexOf("yy") != -1) continue;
  //   result.add(strings.get(i) + "y");
  // }
  // return result;
  
  
  
  // with stream
  List<String> result = new ArrayList<>();
  result = strings.stream()
    .map(n -> n + "y")
    .filter(n -> n.indexOf("yy") == -1)
    .collect(Collectors.toList());
  return result;
}

