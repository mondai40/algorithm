function max1020(a, b){
  const fixedA = in1020(a);
  const fixedB = in1020(b);
  return fixedA > fixedB ? fixedA : fixedB;
}
function in1020(num) {
  return num >= 10 && num <= 20 ? num : 0;
}