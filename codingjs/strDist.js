function strDist(str, sub){
  return strDistHelper(str, sub);
}
function strDistHelper(str, sub) {
  if (str.length < sub.length) return str.length;
  if (str.substring(0, sub.length) === sub && str.substring(str.length - sub.length) === sub) {
    return str.length;
  }
  if (str.substring(0, sub.length) !== sub) {
    return strDistHelper(str.substring(1), sub);
  }
  return strDistHelper(str.substring(0, str.length - 1), sub);
}