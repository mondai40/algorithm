// Catherineは与えられた単語や文章を逆側から読み上げる遊びを友達とやっています。
// 文字列が与えられるので、反転した文字列を返す関数を再帰を使って定義してください。

// reversedString('abcd'); => 'dcba'

// The following answer doesn't use a recursion
// function reversedString(str) {
//   const strLen = str.length;
//   if (strLen < 1) return str;
//   let result = '';
//   for (let i = strLen - 1; i >= 0; i--) {
//     result += str[i];
//   }
//   return result;
// }

// fron end to start
// function reversedString(str) {
//   const strLen = str.length;
//   if (strLen < 1) return str;

//   return str.substr(-1) + reversedString(str.substr(0, str.length - 1));
// }

// fron start to end
// function reversedString(str) {
//   const strLen = str.length;
//   if (strLen < 1) return str;

//   return reversedString(str.substr(1)) + str.substr(0, 1);
// }

// role answer
function reversedStringHelper(reversedString, index, originalString) {
  if (reversedString.length >= originalString.length) return reversedString;
  return reversedStringHelper(
    originalString[index] + reversedString,
    ++index,
    originalString
  );
}

function reversedString(str) {
  return reversedStringHelper(str[0], 1, str);
}

console.log(reversedString('abcd'));
console.log(reversedString('I am a developer'));
