function powerN(base, n){
  if (n === 0) return 1
  if (n === 1) return base;
  return powerNHelper(base, n, 1);
}
function powerNHelper(base, n, result) {
  if (n === 1) return result * base;
  return powerNHelper(base, --n, result * base);
}