export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const success = true;
    if (success) {
      resolve('Success');
    }
    reject(new Error('Error'));
  });
}
