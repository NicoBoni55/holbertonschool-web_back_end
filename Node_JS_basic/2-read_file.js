const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = {};
    for (let i = 1; i < lines.length; i += 1) {
      const student = lines[i].split(',');
      if (student.length >= 4) {
        const field = student[3].trim();
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(student[0].trim());
      }
    }
    console.log(`Number of students: ${lines.length - 1}`);
    for (const field in students) {
      if (field) {
        const names = students[field];
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
countStudents("database.csv");