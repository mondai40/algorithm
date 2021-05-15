public int caughtSpeeding(int speed, boolean isBirthday) {
  int addHigher = isBirthday ? 5 : 0;
  if (speed >= 81 + addHigher) return 2;
  if (speed >= 61 + addHigher) return 1;
  return 0;
}

