/* eslint-disable */
export default function returnHowManyArguments(...argument) {
    let argnum = 0;
    for (let i of argument) {
        argnum += 1;
    }
    return argnum;
}
