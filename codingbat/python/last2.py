def last2(str):
  substrNum = 2
  target = str[len(str) - substrNum:]
  count = 0
  for i in range(len(str) - substrNum):
    if str[i:i + substrNum] == target:
      count += 1
  return count
