public List<Integer> no9(List<Integer> nums) {
  // nums.removeIf(n -> n % 10 == 9);
  // return nums;
  return nums.stream().filter(n -> n % 10 != 9).collect(Collectors.toList());
}

