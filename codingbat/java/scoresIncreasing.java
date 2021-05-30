public boolean scoresIncreasing(int[] scores) {
  int prevScore = scores[0];
  for (int score: scores) {
    if (score < prevScore) return false;
    prevScore = score;
  }
  return true;
}

