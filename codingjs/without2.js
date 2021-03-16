function without2(str: string): string {
  if (str.length < 2) return str;
  if (str.length == 2) return '';
  const firstTwo = str.substring(0, 2);
  const lastTwo = str.substring(str.length - 2);
  return firstTwo === lastTwo ? str.substring(2) : str;
}