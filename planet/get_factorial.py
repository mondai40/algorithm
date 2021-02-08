def get_factorial(n):
    return get_factorial_helper(n, 1)
    
def get_factorial_helper(n, result):
    if n == 1: return result
    result *= n
    n -= 1
    return get_factorial_helper(n, result)
    
print(get_factorial(4))
print(get_factorial(10))
