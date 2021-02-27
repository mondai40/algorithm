function array11(nums, i){
  if (i >= nums.length) return 0;
  if (nums[i] === 11) {
    return 1 + array11(nums, ++i);
  } else {
    return array11(nums, ++i);
  }
}