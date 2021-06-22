public List<String> noLong(List<String> strings) {
  // strings.removeIf(n -> n.length() >= 4);
  // return strings;
  
  List<String> result = new ArrayList<>();
  result = strings.stream()
    .filter(n -> n.length() < 4)
    .collect(Collectors.toList());
  return result;
}

