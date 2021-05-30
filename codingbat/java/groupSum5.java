public boolean groupSum5Helper(int start, int[] nums, int target) {
  if (start >= nums.length) return target == 0;
  if (nums[start] % 5 == 0) {
    if (start != nums.length - 1 && nums[start + 1] == 1) return groupSum5Helper(start + 2, nums, target - nums[start]);
    else return groupSum5Helper(start + 1, nums, target - nums[start]);
  }
  if (groupSum5Helper(start + 1, nums, target - nums[start])) return true;
  if (groupSum5Helper(start + 1, nums, target)) return true;
  return false;
}

public boolean groupSum5(int start, int[] nums, int target) {
  return groupSum5Helper(start, nums, target);
}

