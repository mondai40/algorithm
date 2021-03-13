function has271(nums: number[]): boolean{
  // the answer is something wrong
  if (nums.lenght < 3) return false;
  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] === 2 && nums[i+1] === 7 && nums[i+2] === 1) return true
  }
  return false;
}