function zeroMax(nums){
  const result = [];
  let maxOdd = 0;
  for (let i = nums.length - 1; i >= 0; i--) {
    if (nums[i] === 0) {
      result.unshift(maxOdd);
    } else if (nums[i] % 2 === 1) {
      result.unshift(nums[i]);
      maxOdd = nums[i] > maxOdd ? nums[i] : maxOdd;
    } else {
      result.unshift(nums[i]);
    }
  }
  return result;
}