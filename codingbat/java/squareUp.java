public int[] squareUp(int n) {
  // 1のスタートする場所は(n-1) + nの場所
  // 置いていく最後の数は1, 1,2, 1,2,3 と前回より+1されていく
  int[] result = new int[(int)Math.pow(n, 2)];
  
  if (n == 0) return result;
  
  int lastNum = 1;
  for (int i = n - 1; i < result.length; i += n) {
    int index = i;
    for (int j = 1; j <= lastNum; j++) {
      result[index] = j;
      index--;
    }
    lastNum++;
  }
  return result;
}

