function mirrorEnds(string: string):  string {
  if (string.length < 2) return string;
  return mirrorEndsHelper(string, 0, "");
}
function mirrorEndsHelper(string, index, result) {
  if (index > string.length) return result;
  if (string.substr(index, 1) === string.substr(string.length - (index + 1) , 1) {
    result += string.substr(index, 1)
    return mirrorEndsHelper(string, ++index, result);
  } else {
    return result;
  }
}