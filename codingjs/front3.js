function front3(str){
  return front3Helper(str.substring(0, 3), '', 3);
}
function front3Helper(front3, result, copyCount) {
  if (copyCount === 0) return result;
  return front3Helper(front3, result + front3, --copyCount);
}