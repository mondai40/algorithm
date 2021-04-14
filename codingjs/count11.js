function count11(str: string){
  if (str.length < 2) return 0;
  if (str === "11") return 1;
  return count11Helper(str, 0, 0);
}
function count11Helper(str: string, index: number, count: number) {
  if (index >= str.length - 1) return count;
  if (str.substr(index, 2) === "11") {
    count++;
    index += 2;
  } else {
    index++;
  }
  return count11Helper(str, index, count);
}