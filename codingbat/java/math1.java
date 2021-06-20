public List<Integer> math1(List<Integer> nums) {
  // nums.replaceAll(num -> (num + 1) * 10);
  // return nums;
  
  List<Integer> result = new ArrayList<>();
  result = nums.stream()
    .map(num -> (num + 1) * 10)
    .collect(Collectors.toList());
  return result;
}

