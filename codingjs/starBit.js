function starBit(str){
  if (str.length < 2) return "";
  return starBitHelper(str, 0, false, false, "");
}
function starBitHelper(str, index, isStart, isEnd, result) {
  if (isEnd) return result;
  if (str[index] === "-") isStart = true;
  if (isStart && !isEnd) result += str[index];
  if (str[index] === "*") isEnd = true;
  return starBitHelper(str, ++index, isStart, isEnd, result);
}