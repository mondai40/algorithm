def get_lcm(n1, n2):
    lcm = max(n1, n2)
    while lcm % n1 != 0 or lcm % n2 != 0:
        lcm += 1
    return lcm

print(get_lcm(4, 5))
print(get_lcm(4, 6))
print(get_lcm(2, 121))

