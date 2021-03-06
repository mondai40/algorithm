public List<String> copies3(List<String> strings) {
  // List<String> result = new ArrayList<String>(strings.size());
  // int copyTimes = 3;
  // for (String word: strings) {
  //   String newWord = makeCopy(word, copyTimes);
  //   result.add(newWord);
  // }
  // return result;
  
  // with lamda
  // strings.replaceAll(n -> n + n + n);
  // return strings;
  
  // with lamda and stream
  List<String> result = new ArrayList<String>(strings.size());
  result = strings.stream()
    .map(n -> n + n + n)
    .collect(Collectors.toList());
  return result;
}

// public String makeCopy(String word, int copyTimes) {
//   String newWord = "";
//   for (int i = 0; i < copyTimes; i++) {
//     newWord += word;
//   }
//   return newWord;
// }
