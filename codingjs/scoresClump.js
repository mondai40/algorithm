function scoresClump(scores: number[]): boolean {
  if (scores.length <= 2) return false;
  return scoresClumpHelper(scores, 2);
}
function scoresClumpHelper(scores: number[], index: number): boolean {
  if (index >= scores.length) return false;
  if (scores[index] - scores[index - 2] <= 2 && scores[index] - scores[index - 1] <= 2) return true
  return scoresClumpHelper(scores, ++index);
}