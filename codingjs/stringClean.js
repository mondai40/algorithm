function stringClean(str){
  if (str.length < 2) return str;
  return stringCleanHelper(str, 1, str[0], str[0]);
}
function stringCleanHelper(str, index, prevChar, result) {
  if (index >= str.length) return result;
  if (str[index] !== prevChar) {
    result += str[index];
    prevChar = str[index];
  };
  return stringCleanHelper(str, ++index, prevChar, result);
}