function fizzArray3(start, end){
  if (start === end) return [];
  const result = [];
  for (let i = start; i < end; i++) {
    result.push(i);
  }
  return result;
}