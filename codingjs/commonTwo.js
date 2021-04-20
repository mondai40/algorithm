function commonTwo(a, b){
  const aMap = {};
  for (const v of a) {
    if (aMap[v] === undefined) aMap[v] = 1;
    else aMap[v] += 1;
  }
  const result = [];
  for (let i = 0; i < b.length; i++) {
    if (aMap[b[i]] !== undefined && result.indexOf(b[i]) === -1) {
      result.push(b[i]);
    }
  }
  return result.length;
}