def caught_speeding(speed, is_birthday):
  upper_extra = 5 if is_birthday else 0
  if speed <= 60 + upper_extra: return 0
  if speed <= 80 + upper_extra: return 1
  return 2

