function withoutX2(str: string): string {
  if (str.length === 0) return "";
  if (str.length === 1) return str === "x" ? "" : str;
  return withoutX2Helper(str, 0, "");
}
function withoutX2Helper(str: string, index: number, result: string): string {
  if (index >= 2) return result + str;
  if (str[0] === "x") {
    return withoutX2Helper(str.substring(1), ++index, result + "");
  } else {
    return withoutX2Helper(str.substring(1), ++index, result + str[0]);
  }
}