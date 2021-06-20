public List<String> moreY(List<String> strings) {
  strings.replaceAll(string -> "y" + string + "y");
  return strings;
}

