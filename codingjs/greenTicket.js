function greenTicket(a, b, c){
  if (a === b && a === c) return 20;
  if (a === b || a === c || b === c) return 10;
  return 0;
}