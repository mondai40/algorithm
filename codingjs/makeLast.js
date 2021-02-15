function makeLast(nums){
  const result = new Array(nums.length * 2).fill(0);
  result[result.length - 1] = nums[nums.length - 1];
  return result;
}