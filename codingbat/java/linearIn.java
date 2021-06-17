public boolean linearIn(int[] outer, int[] inner) {
  // outerとinnerを同時に見て、
  // innerのほうが大きかったらouterのindexを大きくして、
  // outerのほうが大きかったらfalse
  // それ以外（inner == outer）のときはinnernのindexを大きくする
  // （outerも大きくしてしまうとinner = [2, 2], outer = [2, 3]のような場合にfalseになってしまう）
  int innerIndex = 0;
  int outerIndex = 0;
  while (innerIndex < inner.length && outerIndex < outer.length) {
    if (inner[innerIndex] > outer[outerIndex]) {
      outerIndex++;
    } else if (inner[innerIndex] < outer[outerIndex]) {
      return false;
    } else {
      innerIndex++;
    }
  }
  return innerIndex >= inner.length;
}:
