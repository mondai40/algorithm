function mixString(a: string, b: string): string {
  return mixStringHelper(a, b, "")
}
function mixStringHelper(a: string, b: string, result: string): string {
  if (a === "" || b === "") return result + a + b;
  result += (a.substr(0, 1) + b.substr(0, 1))
  return mixStringHelper(a.substring(1), b.substring(1), result)
}