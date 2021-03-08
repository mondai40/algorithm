function in3050(a, b){
  if (in3040(a) && in3040(b)) return true;
  if (in4050(a) && in4050(b)) return true;
  return false;
}
function in3040(num) {
  return num >= 30 && num <= 40;
}
function in4050(num) {
  return num >= 40 && num <= 50;
}