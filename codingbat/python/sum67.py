def sum67(nums):
  is_skip = False
  total = 0
  for num in nums:
    if not is_skip and num == 6:
      is_skip = True
      continue
    if is_skip and num == 7:
      is_skip = False
      continue
    if not is_skip: total += num
  return total

