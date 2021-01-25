function delDel(str){
  if (str.substring(1, 4) === "del") {
    return str.replace('del', '');
  } else {
    return str;
  }
}