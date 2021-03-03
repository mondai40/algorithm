function copyEndy(nums, count){
  return copyEndyHelper(nums, count, [], 0);
}
function copyEndyHelper(nums, count, result, index) {
  if (count === 0) return result;
  if (isEndy(nums[index])) {
    result.push(nums[index])
    count--;
  };
  return copyEndyHelper(nums, count, result, ++index):
}
function isEndy(num) {
  return (num >= 0 && num <= 10) || (num >= 90 && num <= 100)
}