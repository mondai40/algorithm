function loneTeen(a: number, b: number): boolean {
  const ageArray = Array.from(arguments);
  return loneTeenHelper(ageArray, 0);
}
function loneTeenHelper(ages: number[], count): boolean {
  if (ages.length === 0) return count === 1;
  if (ages[0] >= 13 && ages[0] <= 19) count++;
  return loneTeenHelper(ages.slice(1), count);
}