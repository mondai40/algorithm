def get_permutations(data):
    if len(data) == 0: return []
    if len(data) == 1: return [data]
    
    permutations = []
    for i in range(len(data)):
        current = data[i]
        target_permutation = data[:i] + data[i + 1:]
        permutation_list = get_permutations(target_permutation)
        
        for p in permutation_list:
            permutations.append([current] + p)

    return permutations

data = [1, 2, 3, 4]
permutations = get_permutations(data)
for p in permutations:
    print(p)
