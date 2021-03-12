function array667(nums: number[]): number {
  let count = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] === 6 && (nums[i + 1] === 6 || nums[i + 1] === 7)) count++;
  }
  return count;
}