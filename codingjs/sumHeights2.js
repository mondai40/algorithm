function sumHeights2(heights, start, end){
  if (start === end) return 0;
  let height = 0;
  for (let i = start + 1; i <= end; i++) {
    if (heights[i - 1] <= heights[i]) {
      height += (heights[i] - heights[i - 1]) * 2;
    } else {
      height += heights[i - 1] - heights[i]
    }
  }
  return height;
}