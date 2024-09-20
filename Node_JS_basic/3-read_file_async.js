const fs = require('fs');

async function countStudents(path) {
  try {
    await fs.promises.access(path, fs.constants.F_OK);
    const data = await fs.promises.readFile(path, 'utf8');
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
    let result = `Number of students: ${lines.length - 1}\n`;
    for (const field in students) {
      if (field) {
        const names = students[field];
        result += (`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }
    }
    return result;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
