const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const data = process.argv[2];
      const studentsList = await countStudents(data);
      res.write(studentsList);
    } catch (err) {
      res.write(`Error: ${err.message}`);
    }
    res.end();
  }
});

app.listen(1245);

module.exports = app;
