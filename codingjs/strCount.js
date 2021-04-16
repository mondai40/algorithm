function strCount(str, sub){
  return strCountHelper(str, sub, 0, 0);
}
function strCountHelper(str, sub, index, count) {
  if (index > str.length) return count;
  if (str.substr(index, sub.length) === sub) {
    count++;
    index += sub.length;
  } else {
    index++;
  }
  return strCountHelper(str, sub, index, count);
}