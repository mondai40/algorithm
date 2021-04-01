function frontPiece(nums){
  if (nums.length < 3) return nums;
  return nums.slice(0, 2);
}