const fs = require('node:fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const Students = lines.slice(1);
        const fields = {}
        Students.forEach((Student) => {
            infos = Student.split(',').map((info) => info.trim());
            if (infos.length === 4) {
                const field = infos[3];
                const firstName = infos[0];
                if (!fields[field]) {
                    fields[field] = []
                }
                fields[field].push(firstName);
            }
        });
        console.log(`Number of students: ${Students.length}`);
        for (let field in fields)
            console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`)
    }
    catch (err) {
        throw new Error('Cannot load the database');
    }
}
module.exports = countStudents
