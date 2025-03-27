/* eslint-disable */
export default function createReportObject(employeesList) {
    return {
        allEmployees: employeesList,
        getNumberOfDepartments(employeesList) {
            let num = 0;
            for (let x in employeesList)
                num += 1;
            return num;
        }
    }
}
