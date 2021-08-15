public List<Integer> two2(List<Integer> nums) {
  // with lamda
  // nums.removeIf(n -> n % 5 == 1);
  // nums.replaceAll(n -> n * 2);
  // return nums;
  
  // with stream
  List<Integer> result = new ArrayList<Integer>();
  result = nums.stream()
    .filter(n -> n % 5 != 1)
    .map(n -> n * 2)
    .collect(Collectors.toList());
  return result;
}

