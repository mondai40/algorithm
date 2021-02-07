def binary_search(list, target):
    lowest_index = 0
    highest_index = len(list) - 1

    if list[lowest_index] >= target and list[highest_index] <= target:
        while lowest_index <= highest_index:
            middle_index = (lowest_index + highest_index) // 2
            if list[middle_index] > target:
                highest_index = middle_index
            elif list[middle_index] < target:
                lowest_index = middle_index
            else:
                return middle_index
    return f"There is no {target}" 



num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_index = binary_search(num_list, 11)
print(f"index is {find_index}")
