'use strict';

// function count(n) {
//   //base case
//   if (n === 0) return 0;
//   return 1 + count(n - 1);
// }

function count(start, final) {
  if (start === final) return start;
  console.log(start);
  return count(++start, final);
}

console.log(count(2, 15));
