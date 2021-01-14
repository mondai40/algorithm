function countX(str: string): number {
  return countXHelper(str, 0);
}
function countXHelper(str: string, count: number): number {
  if (str === "") return count;
  if (str[0] === "x") count++;
  return countXHelper(str.substring(1), count);
}