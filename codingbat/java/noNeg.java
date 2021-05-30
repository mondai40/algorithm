public List<Integer> noNeg(List<Integer> nums) {
  // nums.removeIf(n -> n < 0);
  // return nums;
  return nums.stream().filter(n -> n >= 0).collect(Collectors.toList());
}

