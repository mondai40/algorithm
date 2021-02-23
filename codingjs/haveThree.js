function haveThree(nums){
  if (nums.lenght < 5) return false;
  const numsStr = nums.join('');
  if (numsStr.match(/3/g) != null && numsStr.match(/3/g).length >= 4) return false;
  return /3.3.3/.test(numsStr);
}