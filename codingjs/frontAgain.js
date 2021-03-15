function frontAgain(str){
  if (str.length < 2) return false;
  return str.substring(0, 2) === str.substring(str.length - 2);
}