function stringE(str: string): string{
  let eCount = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "e") eCount++;
  }
  return eCount >= 1 && eCount <= 3;
}