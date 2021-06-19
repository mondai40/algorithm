public Map<String, String> topping3(Map<String, String> map) {
  Map<String, String> result = new HashMap<String, String>(map);
  if (result.containsKey("potato")) result.put("fries", result.get("potato"));
  if (result.containsKey("salad")) result.put("spinach", result.get("salad"));
  return result;
}

