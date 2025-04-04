/* eslint-disable */
export default function getListStudentsIds(arr) {
    if (!Array.isArray(arr)) {
        return [];
    }
    return arr.map(obj => obj.id);
}
