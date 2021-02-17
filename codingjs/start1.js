function start1(a, b){
  const argArr = Array.from(arguments);
  return start1Helper(argArr, 0);
}
function start1Helper(argArr, count) {
  if (argArr.length === 0) return count;
  if (argArr[0][0] === 1) count++;
  return start1Helper(argArr.slice(1), count)
}