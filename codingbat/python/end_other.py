def end_other(a, b):
  lowerA = a.lower();
  lowerB = b.lower();
  
  # with if condition
  # if len(lowerA) >= len(lowerB):
  #   return lowerA[(len(a) - len(b)):] == lowerB
  # else:
  #   return lowerB[(len(b) - len(a)):] == lowerA
  
  # with target.endswitdh(keyword)
  return lowerA.endswith(lowerB) or lowerB.endswith(lowerA)
