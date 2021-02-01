function hasBad(str: string): boolen {
  return hasBadHelper(str, 0);
}
function hasBadHelper(str: string, index): boolena {
  if (index > 1) return false;
  return str.substr(index, 3) === "bad" || hasBadHelper(str, ++index);
}