function sumDigits(str){
  if (str.length < 1) return 0;
  return sumDigitsHelper(str, 0);
}
function sumDigitsHelper(str, sum) {
  if (str.length < 1) return sum;
  if (/[0-9]/.test(str.substr(0, 1))) {
    sum += parseInt(str.substr(0, 1));
  }
  return sumDigitsHelper(str.substr(1), sum);
}