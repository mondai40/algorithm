public int maxMirror(int[] nums) {
  int max = 0;
  
  // 頭から見ていく
  for (int i = 0; i < nums.length; i++) {
    int count = 0;
    // 後ろから見ていく
    // 共通部分がcountを超えても終わり、すべてが共通紙の場合
    for (int j = nums.length - 1; j >= 0 && i + count < nums.length; j--) {
      // 共通部分が一致していれば、count++, 一致してなければmaxとcountを比較
      // 共通部分の抽出は前半部分はi + countで対応
      if (nums[i + count] == nums[j]) {
        count++;
      } else {
        max = Math.max(max, count);
        count = 0;
      }
      max = Math.max(max, count);
    }
  }
  
  return max;
}

