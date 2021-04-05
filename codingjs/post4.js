function post4(nums){
  const lastFourIndex = nums.lastIndexOf(4);
  return [...nums.splice(lastFourIndex + 1)];
}