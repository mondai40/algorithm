function squirrelPlay(temp: number, isSummer: boolean): boolean {
  const maxTemp = isSummer ? 100 : 90;
  return temp >= 60 && temp <= maxTemp;
}