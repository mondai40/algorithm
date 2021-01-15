function scoresIncreasing(scores: number[]): boolean {
  return scoredIncreasingHelper(scores, 1);
}
function scoredIncreasingHelper(scores: number[], index: number): boolean {
  if (index > scores.length) return true;
  if (scores[index] < scores[index - 1]) return false;
  return scoredIncreasingHelper(scores, ++index);
}