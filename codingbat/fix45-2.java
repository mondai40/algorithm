public int[] fix45(int[] nums) {
  for (int i = 0; i < nums.length; i++) {
    if (nums[i] == 4) {
      for (int j = 0; j < nums.length; j++) {
        if (nums[j] == 5) {
          if (j <= 0 || nums[j - 1] != 4) {
            int temp = nums[i + 1];
            nums[i + 1] = nums[j];
            nums[j] = temp;
          }
        }
      }
    }
  }
  return nums;
}

// 4のとき
// 頭からloopして5をさがす
//   index = 0のとき[5]と[4の次の数字]をswap
//   index > 0のとき5の前の数字が
//     4のとき、skip
//     4以外の時、[5]と[4の次の数字]をswap
