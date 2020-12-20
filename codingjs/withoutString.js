function withoutString(base: string, remove: string): string {
  const regex = new RegExp(remove, 'gi');  
  return base.replace(regex, '').replace(/\s+/, ' ');
}