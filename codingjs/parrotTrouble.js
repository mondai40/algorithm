function parrotTrouble(talking: boolean, hour: number): boolean{
  return talking && (hour < 7 || hour > 20);
}