function userCompare(aName, aId, bName, bId){
  if (aName < bName) return -1;
  if (aName > bName) return 1;
  if (aId < bId) return -1;
  if (aId > bId) return 1;
  return 0;
}