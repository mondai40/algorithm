function shareDigit(a: number, b: number): boolean{
  const [onesA, tensA] = [a % 10, Math.floor(a / 10)];
  const [onesB, tensB] = [b % 10, Math.floor(b / 10)];
  return onesA === onesB || onesA === tensB || tensA === onesB || tensA === tensB;
}