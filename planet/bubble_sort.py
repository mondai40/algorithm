# Time complexity is n * (n - 1) = n^2 - n, So n^2 (Quadratic Time complexity)
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

nums = [0, 23, 2, 76, 223, 54, 12]
print(nums)
sorted_nums = bubble_sort(nums)
print(sorted_nums)

