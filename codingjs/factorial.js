function factorial(n){
  return factorialHelper(n, 1);
}
function factorialHelper(n, result) {
  if (n <= 0) return result;
  return factorialHelper(n - 1, result * n);
}