function fizzString(str: string): string {
  if (str.length < 1) return str;
  let result = "";
  if (str.substring(0, 1) === "f") result += "Fizz";
  if (str.substring(str.length - 1) === "b") result += "Buzz";
  return result === "" ? str : result;
}