function allStar(str){
  if (str === "") return "";
  return allStarHelper(str.split(""), 0):
}
function allStarHelper(strList, index) {
  if (index >= strList.length - 1) return strList[index];
  return strList[index] + "*" + allStarHelper(strList, ++index):
}