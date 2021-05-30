public boolean makeBricks(int small, int big, int goal) {
  return (goal >= big * 5) ? (goal - (big * 5)) <= small : (goal % 5) <= small;
}

