function maxMirror(nums){
  if (nums.length < 2) return nums.length;
  let maxLen = 0;
  for (let i = 0; i < nums.length; i++) {
    let count = 0;
    for (let j = nums.length - 1; j >= 0; j--) {
      if (nums[i + count] === nums[j]) {
        count++;
      } else {
        maxLen = count > maxLen ? count : maxLen;
        count = 0;
      }
    }
    maxLen = count > maxLen ? count : maxLen;
  }
  return maxLen;
}