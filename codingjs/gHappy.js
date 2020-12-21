function gHappy(str){
  const customeStr = 'x' + str + 'x';
  return gHappyHelper(customeStr, true);
}
function gHappyHelper(str, happy) {
  if (str.length < 3) return happy;
  if (/gg/.test(str.substring(0, 3))) {
    return gHappyHelper(str.substring(3), true);
  }
  if (/[^g]g[^g]/.test(str.substring(0, 3))) {
    return false;
  }
  return gHappyHelper(str.substring(1), happy);
}