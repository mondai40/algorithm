public boolean splitArrayHelper(int[] nums, int index, int leftSum, int rightSum) {
  if (index >= nums.length) return leftSum == rightSum;
  if (splitArrayHelper(nums, index + 1, leftSum + nums[index], rightSum)) return true;
  if (splitArrayHelper(nums, index + 1, leftSum, rightSum + nums[index])) return true;
  return false;
}

public boolean splitArray(int[] nums) {
  return splitArrayHelper(nums, 0, 0, 0);
}

