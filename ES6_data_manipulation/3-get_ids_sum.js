/* eslint-disable */
export default function getStudentsIdsSum(arr) {
    if (!Array.isArray(arr)) {
        return [];
    }
    return arr.reduce((accumulator, student) => accumulator + student.id, 0);
}
