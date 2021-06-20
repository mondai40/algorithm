public List<String> moreY(List<String> strings) {
  // strings.replaceAll(string -> "y" + string + "y");
  // return strings;
  
  List<String> result = new ArrayList<>();
  result = strings.stream()
    .map(string -> "y" + string + "y")
    .collect(Collectors.toList());
  return result;
}

