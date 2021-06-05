def make_bricks(small, big, goal):
  return small >= goal % 5 if goal <= (big * 5) else small >= goal - (big * 5)

