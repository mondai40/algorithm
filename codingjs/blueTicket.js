function blueTicket(a, b, c){
  if (a + b === 10 || b + c === 10 || a + c === 10) return 10;
  if (Math.abs((a + b) - (b + c)) >= 10 || Math.abs((a + b) - (a + c)) >= 10) return 5;
  return 0;
}