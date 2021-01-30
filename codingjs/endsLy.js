function endsLy(str){
  if (str.length < 3) return str === 'ly';
  return str.substring(str.length - 2) === 'ly';
}