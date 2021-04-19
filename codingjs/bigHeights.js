function bigHeights(heights, start, end){
  let count = 0;
  for (let i = start + 1; i <= end; i++) {
    if (Math.abs(heights[i - 1] - heights[i]) >= 5) count++;
  }
  return count;
}