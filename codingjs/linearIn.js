function linearIn(outer, inner){
  let prevIndex = 0;
  for (let i = 0; i < inner.length; i++) {
    if (outer.indexOf(inner[i]) >= prevIndex) {
      prevIndex = outer.slice(prevIndex).indexOf(inner[i]);
    } else {
      return false;
    }
  }
  return true;
}