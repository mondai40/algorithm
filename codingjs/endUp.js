function endUp(str: string): string {
  return str.substring(0, str.length - 3) + str.substring(str.length - 3).toUpperCase();
}