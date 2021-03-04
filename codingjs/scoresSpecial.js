function scoresSpecial(a, b){
  const largestNumInA = scoresSpecialHelper(a);
  const largestNumInB = scoresSpecialHelper(b);
  return largestNumInA + largestNumInB
}
function scoresSpecialHelper(nums) {
  let maxSpecialScore = 0;
  for (const val of nums) {
    if (val % 10 === 0 && val > maxSpecialScore) {
      maxSpecialScore = val;
    }
  }
  return maxSpecialScore;
}