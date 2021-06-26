def cat_dog(str):
  # add 1 if I got cat, substract 1 if I got dog
  total = 0
  i = 0
  while i < len(str) - 2:
    if str[i:i+3] == "cat":
      total += 1
      i += 3
    elif str[i:i+3] == "dog":
      total -= 1
      i += 3
    else:
      i +=1
  
  return total == 0
  

