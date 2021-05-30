public boolean groupSum6Helper(int start, int[] nums, int target) {
  if (start >= nums.length) return target == 0;
  if (nums[start] == 6) return groupSum6Helper(start + 1, nums, target - nums[start]);
  if (groupSum6Helper(start + 1, nums, target - nums[start])) return true;
  if (groupSum6Helper(start + 1, nums, target)) return true;
  return false;
}

public boolean groupSum6(int start, int[] nums, int target) {
  return groupSum6Helper(start, nums, target);
}

