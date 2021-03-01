function countPairs(str){
  if (str.length < 3) return 0;
  return countPairsHelper(str, 0);
}
function countPairsHelper(str, result) {
  if (str.length < 3) return result;
  if (str.substr(0, 1) === str.substr(2, 1)) {
    result++
  }
  return countPairsHelper(str.substr(1), result)
}