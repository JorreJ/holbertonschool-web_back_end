const fs = require('node:fs');

function countStudents(path) {
  return fs.promises.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const Students = lines.slice(1);
      const fields = {};

      Students.forEach((Student) => {
        const infos = Student.split(',').map((info) => info.trim());
        if (infos.length === 4) {
          const field = infos[3];
          const firstName = infos[0];
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstName);
        }
      });

      console.log(`Number of students: ${Students.length}`);
      for (const field in fields) {
        if (field) {
          console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
        }
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
