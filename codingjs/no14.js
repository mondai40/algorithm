function no14(nums: number[]): boolean {
  const hashmap = new Map();
  for (num of nums) {
    if (num === 1 || num === 4) hashmap.set(num, hashmap.get(num) + 1);
  }
  return hashmap.size < 2:
}