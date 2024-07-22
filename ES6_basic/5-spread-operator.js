export default function concatArrays(array1, array2, string) {
  const array4 = [...array1, ...array2, ...string];
  return (array4);
}
