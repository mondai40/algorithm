// the worst solution
// function fibonacci(n) {
//   if (n === 0) return 0;
//   if (n === 1) return 1;
//   return fibonacci(n - 1) + fibonacci(n - 2);
// }

// the N solution
// const map = new Map();
// map.set(0, 0);
// map.set(1, 1);

// function fibonacci(n) {
//   if (map.has(n)) return map.get(n);
//   const value = fibonacci(n - 1) + fibonacci(n - 2);
//   map.set(n, value);
//   return value;
// }

// the recursion solution
// function fibonacciHelper(f1, f2, n) {
//   if (n === 0) return f1;
//   return fibonacciHelper(f2, f1 + f2, n - 1);
// }

// function fibonacci(n) {
//   return fibonacciHelper(0, 1, n);
// }

// more faster solution
function fibonacci(n) {
  const cache = {};

  function fibonacciHelper(index) {
    if (cache[index]) return cache[index];
    if (index === 0) return 0;
    if (index === 1) return 1;
    cache[index] = fibonacciHelper(index - 1) + fibonacciHelper(index - 2);
    return cache[index];
  }

  return fibonacciHelper(n);
}

console.log(fibonacci(5));
console.log(fibonacci(9));
console.log(fibonacci(100));
