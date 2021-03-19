function sameStarChar(str: string): boolean {
  if (str.length < 3) return true;
  for (let i = 1; i < str.length - 1; i++) {
    if (str[i] === "*") {
      if (str[i -1] !== str[i + 1]) return false;
    }
  }
  return true;
}