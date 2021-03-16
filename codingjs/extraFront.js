function extraFront(str: string): string {
  const target = str.length < 2 ? str : str.substring(0, 2);
  const copyCount = 3;
  return extraFrontHelper(str, "", target, copyCount);
}
function extraFrontHelper(str: string, result: string, target: string, copyCount: number): string {
  if (copyCount === 0) return result;
  result += target;
  return extraFrontHelper(str, result, target, --copyCount);
}