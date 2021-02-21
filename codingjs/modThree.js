function modThree(nums: number[]): boolean {
  if (nums.length < 3) return false;
  let evenCount = 0;
  let oddCount = 0;
  let prevNum = nums[0]
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] % 2 === 0 && prevNum % 2 === 0) {
      evenCount++;
      oddCount = 0;
    }
    if (nums[i] % 2 === 1 && prevNum % 2 === 1) {
      oddCount++;
      evenCount = 0;
    }
    prevNum = nums[i];
  }
  return evenCount === 2 || oddCount === 2;
}