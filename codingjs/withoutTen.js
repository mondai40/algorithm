function withoutTen(nums){
  const result = new Array(nums.length).fill(0);
  let inputIndex = 0;
  for (const num of nums) {
    if (num % 10 === 0) continue;
    result[inputIndex] = num;
    inputIndex++;
  }
  return result;
}