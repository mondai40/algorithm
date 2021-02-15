function no23(nums){
  const hash_map = new Array(nums.length).fill(false);
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 2 || nums[i] === 3) hash_map[i] = true;
  }
  return hash_map.indexOf(true) == -1  
}