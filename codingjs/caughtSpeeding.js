function caughtSpeeding(speed: number, isBirthday: boolean): number {
  const addSpeedLimit = isBirthday ? 5 : 0;
  if (speed <= 60 + addSpeedLimit) return 0;
  if (speed <= 80 + addSpeedLimit) return 1;
  return 2;
}