function dividesSelf(n){
  let target = n;
  let remainder = 0;
  while (target > 0) {
    remainder = target % 10;
    if (remainder === 0 || n % remainder != 0) {
      return false;
    }
    target = Math.floor(target / 10);
  }
  return true;
}