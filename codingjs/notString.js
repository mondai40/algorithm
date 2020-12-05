function notString(str: string): string{
  if (str.substring(0, 3) === 'not') return str;
  return 'not ' + str;
}