function endOther(a: string, b: string): boolean {
  if (a.length > b.length) {
    const longStr = a.toLowerCase();
    const shortStr = b.toLowerCase();
  } else {
    const shortStr = a.toLowerCase();
    const longStr = b.toLowerCase();
  }
  return (longStr.substr(0, shortStr.length) === shortStr) 
          || (longStr.substr(-1 * shortStr.length) === shortStr;
  //the result is wrong
}