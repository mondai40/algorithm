function endX(str){
  return endXHelper(str, "", 0);
}
function endXHelper(str, result, xs) {
  if (str === "") return result + ("x".repeat(xs));
  if (str.substr(0, 1) === "x") {
    xs++;
  } else {
    result = result + str.substr(0, 1);
  }
  return endXHelper(str.substr(1), result, xs);
}