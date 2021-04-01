function unlucky1(nums){
  if (nums.length < 2) return false;
  for (let i = 0; i < nums.length - 1; i++) {
    if (!(i === 0 || i === 1 || i === nums.length - 2)) continue;
    if (nums[i] === 1 && nums[i + 1] === 3) return true; 
  }
  return false;
}