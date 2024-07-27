export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  const result = [];
  for (const item of set) {
    if (item.startsWith(startString)) {
      const newItem = item.slice(startString.length);
      result.push(newItem);
    }
  }
  return result.join('-');
}
