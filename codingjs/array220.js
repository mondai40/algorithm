function array220(nums, i){
  if (i >= nums.length) return false;
  if (i === 0) return array220(nums, ++i);
  if (nums[i] % 10 === 0) return true;
  return array220(nums, ++i);
}