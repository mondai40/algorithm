function deFront(str: string): string {
  return deFrontHelper(str, 0);
}
function deFrontHelper(str: string, index: number): string {
  if (index >= str.length) return "";
  if (index === 0) {
    if (str[index] === "a") {
      return "a" + deFrontHelper(str, ++index);
    } else {
      return "" + deFrontHelper(str, ++index);
    }
  }
  if (index === 1) {
    if (str[index] === "b") {
      return "b" + deFrontHelper(str, ++index);
    } else {
      return "" + deFrontHelper(str, ++index);
    }
  }
  return str[index] + deFrontHelper(str, ++index);
}