public int makeChocolate(int small, int big, int goal) {
  int bigNum = 5;
  int reminder = goal / bigNum <= big ? goal % bigNum : goal - (bigNum * big);
  return small >= reminder ? reminder : -1;
}

