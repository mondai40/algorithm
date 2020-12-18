function xyzThere(str: string): boolean {
  return /[^\.]xyz|^xyz/.test(str);
}