function array123(nums: number[]): boolean {
  if (nums.length < 3) return false;
  return /123/.test(nums.join(""));
}