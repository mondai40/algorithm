function wordsWithout(words, target){
  const result = [];
  for (const val of words) {
    if (val !== target) result.push(val); 
  }
  return result;
}