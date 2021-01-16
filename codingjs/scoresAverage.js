function scoresAverage(scores: number[]): number {
  if (scores.length === 2) return scores[0] > scores[1] ? scores[0] : scores[1]
  const halfIndex = scores.length / 2;
  const firstHalfAvg = getArrSum(scores.slice(0, halfIndex), 0, 0);
  const secondHalfAvg = getArrSum(scores.slice(halfIndex), 0, 0);
  return firstHalfAvg > secondHalfAvg ? firstHalfAvg : secondHalfAvg;
}
function getArrSum(halfScores: number[], index: number, sum: number): number {
  if (index >= halfScores.length) return sum / index
  return getArrSum(halfScores, ++index, sum + halfScores[index - 1]);
}