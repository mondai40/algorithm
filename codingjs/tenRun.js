function tenRun(nums){
  const result = [];
  let base = 1;
  for (const num of nums) {
    if (num % 10 === 0) base = num;
    if (base != 1) {
      result.push(base);
    } else {
      result.push(num);
    }
  }
  return result;
}