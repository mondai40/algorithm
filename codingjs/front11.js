function front11(a, b){
  const lenA = a.length;
  const lenB = b.length;
  if (lenA >= 1 && lenB >= 1) return [a[0], b[0]];
  if (lenA === 0 && lenB >= 1) return [b[0]];
  if (lenA >= 1 && lenB === 0) return [a[0]];
  return [];
}