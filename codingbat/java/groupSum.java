public boolean groupSumHelper(int start, int[] nums, int target) {
  if (start >= nums.length) return target == 0;
  // 配列の頭から引き算をしていく再帰
  if (groupSumHelper(start + 1, nums, target - nums[start])) return true;
  // 上記の再帰の途中でfalseになった場合の再帰。引き算をせずに次の配列で再帰
  if (groupSumHelper(start + 1, nums, target)) return true;
  // 上記2つの再帰が成り立たないならfalse
  return false;
}

public boolean groupSum(int start, int[] nums, int target) {
  return groupSumHelper(start, nums, target);
}

