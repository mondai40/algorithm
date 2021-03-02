function copyEvens(nums, count){
  return copyEvensHelper(nums, count, 0, []);
}
function copyEvensHelper(nums, count, index, result) {
  if (index >= nums.length || count === 0) return result;
  if (nums[index] % 2 === 0) {
    result.push(nums[index]);
    count--;
  }
  return copyEvensHelper(nums, count, ++index, result)
}