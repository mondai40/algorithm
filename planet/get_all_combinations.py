def get_all_combinations(s1, s2, s3):
    for i in range(len(s1)):
        for j in range(len(s2)):
            for k in range(len(s3)):
                print(f"{s1[i]} {s2[j]} {s3[k]}")
    
s1 = ["I", "He"]
s2 = ["play", "love"]
s3 = ["Baseball", "Tennis"]
get_all_combinations(s1, s2, s3)
