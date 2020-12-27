function makeBricks(small, big, goal){
  if (goal > big * 5) {
    return goal - (big * 5) <= small;
  } else {
    return (goal % 5) - small <= 0;
  }
}