function rotateLeft3(nums: number[]): number[]{
  const firstNum = nums.shift();
  nums.push(firstNum);
  return nums;
}
