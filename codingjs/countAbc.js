function countAbc(str){
  if (str.length < 3) return 0;
  if (str === "abc" || str === "aba") return 1;
  return countAbcHelper(str, 0, 0);
}
function countAbcHelper(str, index, count) {
  if (index >= str.length - 2) return count;
  const target = str.substr(index, 3);
  if (target === "abc" || target === "aba") count++
  return countAbcHelper(str, ++index, count);
}