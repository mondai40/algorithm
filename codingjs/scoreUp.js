function scoreUp(key, answers){
  return scoreUpHelper(key, answers, 0, 0);
}
function scoreUpHelper(key, answers, index, score) {
  if (index >= key.length) return score;
  switch (answers[index]) {
    case key[index]:
      score += 4;
      break;
    case "?":
      break
    default:
      score--;
      break;
  }
  return scoreUpHelper(key, answers, ++index, score)
}