function stringMatch(a: string, b: string): number {
  if (a.length < 2 || b.length < 2) return 0;
  return stringMatchHelper(a, b, 0, 0);
}
function stringMatchHelper(a, b, index, result) {
  if (index > a.length - 2 && index > b.length - 2) return result;
  if (a.substr(index, 2) == b.substr(index, 2)) {
    const newResult = index;
    return stringMatchHelper(a, b, ++index, newResult);
  } else {
    return stringMatchHelper(a, b, ++index, result);
  }
  
}