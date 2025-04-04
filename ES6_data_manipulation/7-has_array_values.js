/* eslint-disable */
export default function setFromArray(set, arr) {
    return arr.every(element => set.has(element));
}
