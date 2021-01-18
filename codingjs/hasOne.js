function hasOne(n: number): number {
  return hasOneHelper(n);
}
function hasOneHelper(n: number): number {
  if (n < 10 && n != 1) return false;
  if (n % 10 === 1) {
    return true;
  } else {
    return hasOneHelper(Math.floor(n / 10));
  }
}