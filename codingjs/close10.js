function close10(a, b){
  const numArr = Array.from(arguments);
  let nearestTen = numArr[0];
  let diff = Math.abs(10 - numArr[0]);
  for (let i = 1; i < numArr.length; i++) {
    if (diff > Math.abs(10 - numArr[i])) {
      nearestTen = numArr[i];
    } else if (diff === Math.abs(10 - numArr[i])) {
      nearestTen = 0;
    }
    diff = Math.abs(10 - numArr[i]);
  }
  return nearestTen;
}