function countClumps(nums){
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === nums[i + 1]) {
      count++;
      for (let j = i + 2; j < nums.length; j++) {
        if (nums[i] !== nums[j]) break;
      }
      i = j - 1;
    }
  }
  return count;
}