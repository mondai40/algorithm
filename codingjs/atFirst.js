function atFirst(str){
  if (str.length === 0) return "@@";
  if (str.length === 1) return str + "@";
  return str.substring(0, 2);
}