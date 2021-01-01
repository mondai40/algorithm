function reverse3(nums){
  if (nums.length === 1) return nums[0];
  const poppedNum = nums.pop();
  return [poppedNum, ...reverse3(nums)]
}