function nestParen(str){
  if (str.length === 0) return true;
  if (str[0] === "(" && str[str.length - 1] === ")") {
    return nestParen(str.substring(1, str.length - 1));
  }
  return false;
}