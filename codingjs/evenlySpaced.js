function evenlySpaced(a, b, c){
  const newArr = [a, b, c];
  newArr.sort((x, y) => x - y);
  return newArr[2] - newArr[1] === newArr[1] - newArr[0];
}