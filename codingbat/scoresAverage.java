public int scoresAverage(int[] scores) {
  // if (scores.length < 2) return false;
  int centerPos = scores.length / 2;
  int firstHalfAvg = average(scores, 0, centerPos);
  int secondHalfAvg = average(scores, centerPos, scores.length);
  return firstHalfAvg > secondHalfAvg ? firstHalfAvg : secondHalfAvg;
}

public int average(int[] scores, int start, int end) {
  int sumNum = 0;
  for (int i = start; i < end; i++) {
    sumNum += scores[i];
  }
  return sumNum / (end - start);
}

//(end - start) in line 14 is tricky
