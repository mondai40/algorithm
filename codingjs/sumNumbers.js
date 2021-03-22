function sumNumbers(str: string){
  let result = 0;
//   let isDigit = false;
  let num = "0";
  for (let i = 0; i < str.length; i++) {
    if (/[0-9]/.test(str[i])) {
//       isDigit = true;
      num += str[i];
    } else {
      result += Number(num);
      num = "";
    }
  }
  result += Number(num);
  return result; 
}