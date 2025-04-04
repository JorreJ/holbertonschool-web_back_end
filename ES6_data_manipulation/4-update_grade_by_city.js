/* eslint-disable */
export default function updateStudentGradeByCity(arr, city, newGrades) {
    if (!Array.isArray(arr)) {
        return [];
    }
    return arr
    .filter(student => student.location == city)
    .map((student) => {
		const newGrade = newGrades.find(({ studentId }) => studentId === student.id);
		return {
		  ...student,
		  grade: newGrade ? newGrade.grade : 'N/A',
		};
	  });;
}
