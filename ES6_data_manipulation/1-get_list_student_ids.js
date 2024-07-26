export default function getListStudentIds(list) {
  if (!Array.isArray(list)) {
    return [];
  }
  if (!list.every((item) => typeof item === 'object')) {
    return [];
  }
  return list.map((item) => item.id);
}
