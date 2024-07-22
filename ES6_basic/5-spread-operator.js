export default function concatArrays(array1, array2, string) {
  const array3 = Array.from(string);
  const array4 = [...array1, ...array2, ...array3];
  return (array4);
}
