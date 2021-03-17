function startWord(str:string, word:string):string {
  if (str.length < word.length) return "";
  if (word.length < 2) return str.substring(0, word.length);
  
  if (str.substring(1, word.length) === word.substring(1)) {
    return str.substring(0, word.length)
  } else {
    return "";
  }
}