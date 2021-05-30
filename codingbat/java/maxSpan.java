// I think the problem description is wrong, this code should return the biggest span 
// which leftmost and rightmost has the "same" value
public int maxSpan(int[] nums) {
  if (nums.length < 1) return 0;
  
  int maxSpan = 0;
  for (int i = 0; i < nums.length; i++) {
    for (int j = nums.length - 1; j >= 0; j--) {
      if (nums[i] == nums[j]) {
        int span = j - i + 1;
        maxSpan = span > maxSpan ? span : maxSpan;
      }
    }
  }
  return maxSpan;
}

