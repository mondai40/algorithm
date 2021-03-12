function noTriples(nums: number[]): boolean {
  let prevNum = nums[0];
  let sameNumCount = 1;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] === prevNum) {
      sameNumCount++;
      if (sameNumCount >= 3) return false;
    } else {
      prevNum = nums[i];
      sameNumCount = 1;
    }
  }
  return true;
}