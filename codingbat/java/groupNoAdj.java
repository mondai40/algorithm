public boolean groupNoAdjHelper(int start, int[] nums, int target) {
  if (start >= nums.length) return target == 0;
  if (groupNoAdjHelper(start + 2, nums, target - nums[start])) return true;
  if (groupNoAdjHelper(start + 1, nums, target)) return true;
  return false;
}

public boolean groupNoAdj(int start, int[] nums, int target) {
  return groupNoAdjHelper(start, nums, target);
}

