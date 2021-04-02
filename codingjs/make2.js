function make2(a, b){
  if (a.length >= 2) return [a[0], a[1]];
  if (a.length >= 1) return [a[0], b[0]]
  if (a.length <= 0) return [b[0], b[1]];
}