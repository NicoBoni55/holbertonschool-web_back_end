export default function getStudentsByLocation(list, city) {
  if (typeof city !== 'string') {
    return list;
  }
  return list.filter((item) => item.location === city);
}
