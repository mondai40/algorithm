function countYZ(str: string): number {
  if (str.length === 0) return 0;
  if (str.toLowerCase() === 'y' || str.toLowerCase() === 'z') return 1;
  const target = str.substring(0, 2).toLowerCase()
  if (/[yz][^a-z]/.test(target)) {
    return 1 + countYZ(str.substring(2));
  }
  return 0 + countYZ(str.substring(1));
}