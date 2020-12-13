function withoutEnd(str: string): string {
  if (str.length < 3) return '';
  return str.substr(1, str.length - 2);
}