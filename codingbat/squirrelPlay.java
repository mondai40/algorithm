public boolean squirrelPlay(int temp, boolean isSummer) {
  int upperTemp = isSummer ? 100 : 90;
  return temp >= 60 && temp <= upperTemp;
}

