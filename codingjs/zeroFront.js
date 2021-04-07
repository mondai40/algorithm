function zeroFront(nums){
  const result = [];
  for (const num of nums) {
    if (num === 0) result.unshift(num);
    else result.push(num);
  }
  return result;
}