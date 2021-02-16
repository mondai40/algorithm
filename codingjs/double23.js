function double23(nums){
  if (nums.length < 2) return false;
  const map = new Map()
  for (let i = 0; i < nums.length; i++) {
    let key = nums[i];
    if (map.has(key)) map.set(key, map.get(key) + 1);
    else map.set(key, 1);
  }
  return map.get(2) === 2 || map.get(3) === 2;
}