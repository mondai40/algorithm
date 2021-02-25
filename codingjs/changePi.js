function changePi(str: string): string {
  return changePiHelper(str, '');
}
function changePiHelper(str: string, result: string): string {
  if (str.length === 0) return result;
  if (str.substr(0, 2) === 'pi') {
    result += '3.14';
    return changePiHelper(str.substr(2), result);
  } else {
    result += str.substr(0, 1);
    return changePiHelper(str.substr(1), result);
  }
}