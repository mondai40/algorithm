function mapAB2(someMap){
  if (someMap.get("a") === someMap.get("b")) {
    someMap.delete("a");
    someMap.delete("b");
  }
  return someMap;
}