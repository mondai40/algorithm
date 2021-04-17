function strCopies(str, sub, n){
  if (str.length < sub.length) return false;
  return strCopiesHelper(str, sub, n, 0, 0);
}
function strCopiesHelper(str, sub, n, index, count) {
  if (index >= str.length) return n === count;
  if (str.substr(index, sub.length) === sub) count++;
  return strCopiesHelper(str, sub, n, ++index, count);
}