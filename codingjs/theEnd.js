function theEnd(str, front){
  if (str.length < 2) return str;
  return front ? str.substr(0, 1) : str.substr(str.length - 1)
}