public Map<String, String> topping2(Map<String, String> map) {
  Map<String, String> result = new HashMap<String, String>(map);
  if (result.containsKey("ice cream")) result.put("yogurt", result.get("ice cream"));
  if (result.containsKey("spinach")) result.put("spinach", "nuts");
  return result;
}

