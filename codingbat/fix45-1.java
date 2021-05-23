public int[] fix45(int[] nums) {
  if (nums.length < 2) return nums;
  for (int i = 0; i < nums.length; i++) {
    if (i <= 0 && nums[i] == 5) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[j] != 4 && nums[j] != 5) {
          int temp = nums[j];
          nums[j] = nums[i];
          nums[i] = temp;
          break;
        }
      }
    } 
    if (i > 0)  {
      if (nums[i] == 5 && nums[i - 1] != 4) {
        for (int j = i + 1; j < nums.length; j++) {
          if (nums[j] != 4 && nums[j] != 5) {
            int temp = nums[j];
            nums[j] = nums[i];
            nums[i] = temp;
            break;
          }
        }
      } else if (nums[i] != 4 && nums[i] != 5 && nums[i - 1] == 4) {
        for (int j = i + 1; j < nums.length; j++) {
          if (nums[j] == 5) {
            int temp = nums[j];
            nums[j] = nums[i];
            nums[i] = temp;
            break;
          }
        }
      }
    }
  }
  
  return nums;
}

// index = 0
// 4なら何もしない、
// 5ならindex + 1からloopして4, 5以外の数字とswap
// 4, 5以外なら何もしない
// index > 0
// 4なら何もしない
// 5ならindex - 1の数字見て
//   4ならそのまま
//   4以外ならindex + 1からloopして4, 5以外の数字とswap
// 4,5以外ならindex - 1の数字見て
//   4ならindex + 1からloopして5とswap
//   4以外ならそのまま
