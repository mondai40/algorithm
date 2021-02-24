function squareUp(n){
  const result = [];
  for (let i = 1; i <= n; i++) {
    for (let j = n; j > 0; j--) {
      if (i >= j) {
        result.push(j);
      } else {
        result.push(0);
      }
    }
  }
  return result;
}