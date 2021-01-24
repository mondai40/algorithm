function hasTeen(a: number, b: number, c: number): bolean {
  const agesArr = Array.from(arguments);
  return hasTeenHelper(agesArr);
}
function hasTeenHelper(ages: number[]): boolean {
  if (ages.length === 0) return false;
  if (ages[0] >= 13 && ages[0] <= 19) return true;
  return hasTeenHelper(ages.slice(1));
}