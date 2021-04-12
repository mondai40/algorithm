function seriesUp(n){
  const result = [];
  for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= i; j++) {
        result.push(j);
      }
  }
  return result;
}

