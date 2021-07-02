def centered_average(nums):
  sum = 0
  minNum = nums[0]
  maxNum = nums[0]
  for num in nums:
    if minNum > num: minNum = num
    if maxNum < num: maxNum = num
    sum += num
  return (sum - minNum - maxNum) / (len(nums) - 2)

