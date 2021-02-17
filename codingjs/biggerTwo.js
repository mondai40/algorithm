function biggerTwo(a, b){
  const aSum = a.reduce((accu, iccu) => accu + iccu, 0);
  const bSum = b.reduce((accu, iccu) => accu + iccu, 0);
  return aSum >= bSum ? a : b;
}