function withoutDoubles(die1, die2, noDoubles){
  if (die1 === die2 && noDoubles) {
    return die1 === 6 ? 7 : die1 * 2 + 1
  }
  return die1 + die2;
}