function mapShare(someMap){
  if (someMap.has('a')) someMap.set('b', someMap.get('a'));
  if (someMap.has('c')) someMap.delete('c');
  return someMap;
}