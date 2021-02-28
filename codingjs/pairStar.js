function pairStar(str){
  if (str === "") return "";
  return pairStarHelper(str.split(""), 0, "");
}
function pairStarHelper(strList, index, prevChar) {
  if (index >= strList.length) return "";
  if (strList[index] === prevChar) {
    const str = "*" + strList[index];
  } else {
    const str = strList[index];
  }
  prevChar = strList[index];
  return str + pairStarHelper(strList, ++index, prevChar);
}