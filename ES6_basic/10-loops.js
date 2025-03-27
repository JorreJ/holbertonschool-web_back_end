/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    let newarray = []
    for (let value of array) {
      newarray.push(appendString + value);
    }
  
    return newarray;
  }
