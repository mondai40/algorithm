function changeXY(str: string): string{
  return changeXYHelper(str, '');
}
function changeXYHelper(str: string, result: string): string {
  if (str.length === 0) return result;
  if (str.substr(0, 1) === 'x') {
    result += 'y';
  } else {
    result += str.substr(0, 1);
  }
  return changeXYHelper(str.substr(1), result);
}