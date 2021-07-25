def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
  remainder = num % 10
  quotient = num // 10
  return (quotient + 1) * 10 if remainder >= 5 else quotient * 10

