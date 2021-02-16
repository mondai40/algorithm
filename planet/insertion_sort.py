def insertion_sort(nums):
    for i in range(len(nums)):
        target = nums[i]
        j = i - 1
        while target < nums[j] and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = target
    return nums


nums = [12, 11, 13, 5, -6]
print(nums)
sorted_nums = insertion_sort(nums)
print(sorted_nums)
