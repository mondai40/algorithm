def get_abs_diff(a, b):
  return abs(a - b)
  
def diff21(n):
  target_int = 21
  abs_diff = get_abs_diff(n, target_int)
  return abs_diff * 2 if n > 21 else abs_diff

