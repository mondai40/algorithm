function canBalance(nums){
  for (let i = 0; i < nums.length - 1; i++) {
    const firstHalfSum = nums.slice(0, i + 1).reduce((a, c) => a + c);
    const secondHalfSum = nums.slice(i + 1).reduce((a, c) => a + c);
    if (firstHalfSum === secondHalfSum) return true
  }
  return false;
}