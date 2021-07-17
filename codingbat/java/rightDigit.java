public List<Integer> rightDigit(List<Integer> nums) {
  
  // normal solution
  // List<Integer> result = new ArrayList<>();
  // for (int i = 0; i < nums.size(); i++) {
  //   result.add(nums.get(i) % 10);
  // }
  // return result;
  
  // with lambda
  nums.replaceAll(n -> n % 10);
  return nums;
  
  // with stream
  // nums = nums.stream()
  //   .map(n -> n % 10)
  //   .collect(Collectors.toList());
  // return nums;
}

