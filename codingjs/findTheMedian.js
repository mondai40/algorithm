function findTheMedian(nums){
  if (nums.length % 2 === 0) {
    return (nums[nums.length / 2 - 1] + nums[nums.length / 2]) / 2
  } else {
    return nums[Math.floor(nums.length / 2)];
  }
}