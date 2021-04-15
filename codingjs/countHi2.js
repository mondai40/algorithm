function countHi2(str){
  if (str < 2) return 0;
  return countHi2Helper(str, 0, 0);
}
function countHi2Helper(str, index, count) {
  if (index >= str.length - 1) return count;
  if (str.substr(index, 2) === "hi" && str[index - 1] !== "x") {
    index += 2;
    count++;
  } else {
    index++;
  }
  return countHi2Helper(str, index, count);
}