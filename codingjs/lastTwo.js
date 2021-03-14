function lastTwo(str: string): string {
  if (str.length < 2) return str;
  const firstFromLast = str[str.length - 1];
  const secondFromLast = str[str.length - 2]
  return str.substring(0, str.length - 2) + firstFromLast + secondFromLast;
}