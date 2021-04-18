function sumHeights(heights, start, end){
  if (start === end) return 0;
  let height = 0;
  for (let i = start + 1; i <= end; i++) {
    height += Math.abs(heights[i] - heights[i - 1]);
  }
  return height;
}