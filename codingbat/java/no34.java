public List<String> no34(List<String> strings) {
  // strings.removeIf(n -> n.length() == 3 || n.length() == 4);
  // return strings;
  
  List<String> result = new ArrayList<>();
  result = strings.stream()
    .filter(n -> n.length() < 3 || n.length() > 4)
    .collect(Collectors.toList());
  return result;
}

