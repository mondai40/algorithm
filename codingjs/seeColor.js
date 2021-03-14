function seeColor(str: string):string {
  if (/^red/.test(str)) return "red";
  if (/^blue/.test(str)) return "blue";
  return "";
}