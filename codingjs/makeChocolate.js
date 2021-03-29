function makeChocolate(small, big, goal){
  //the test case makeChocolate(1, 2, 7) → 2 is wrong.
  let remainder = 0;
  remainder = goal >= big * 5 ? goal - (big * 5) : goal % 5;
  return remainder <= small ? remainder : -1;
}