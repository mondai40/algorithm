function mergeTwo(a, b, n){
  const result = [];
  let aIndex = 0;
  let bIndex = 0;
  for (let i = 0; i < n; i++) {
    if (a[aIndex] < b[bIndex]) {
      result.push(a[aIndex]);
      aIndex++;
      continue;
    }
    if (a[aIndex] > b[bIndex]) {
      result.push(b[bIndex]);
      bIndex++;
      continue;
    }
    if (a[aIndex] === b[bIndex]) {
      result.push(a[aIndex]);
      aIndex++;
      bIndex++;
    }
  }
  return result;
}