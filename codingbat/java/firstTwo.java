public String firstTwo(String str) {
  String extractedWord = str.length() < 2 ? str : str.substring(0, 2);
  return extractedWord;
}

