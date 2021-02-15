# Time complexity is 1 / 2 * n * (a + (a + (n - 1) * d)), O(n ^ 2)(Quadratic Time Complexity)
def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    
    return list

num_list = [2, 1, 1000, 100, -2]
print(selection_sort(num_list))
