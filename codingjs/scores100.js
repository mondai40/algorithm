function scores100(scores: number[]): boolean {
  return scores100Helper(scores, 1);
}
function scores100Helper(scores: number[], index: number): boolean {
  if (index > scores.length) return false;
  if (scores[index] === 100 && scores[index - 1] === 100) return true;
  return scores100Helper(scores, ++index);
}