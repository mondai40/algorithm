def get_lcm(n1, n2):
    for i in range(1, n2 + 1):
        if (n1 * i) % n2 == 0: return n1 * i

print(get_lcm(4, 5))
print(get_lcm(4, 6))
print(get_lcm(2, 121))
