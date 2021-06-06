def big_diff(nums):
  max_num = nums[0]
  min_num = nums[0]
  for num in nums:
    if num > max_num: max_num = num
    if num < min_num: min_num = num
  return max_num - min_num

