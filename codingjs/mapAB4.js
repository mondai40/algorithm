function mapAB4(someMap){
//   return someMap;
  if (someMap.has("a") && someMap.has("b")) {
    const aLength = someMap.get("a").length;
    const bLength = someMap.get("b").length;
    if (aLength > bLength) {
      someMap.set("c", someMap.get("a"));
    } else if (aLength < bLength) {
      someMap.set("c", someMap.get("b"));
    } else {
      someMap.set("a", "");
      someMap.set("b", "");
    }
  }
  return someMap;
}