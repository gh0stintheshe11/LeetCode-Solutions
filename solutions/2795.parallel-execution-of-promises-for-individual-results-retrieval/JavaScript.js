/**
 * @param {Array<Function>} functions
 * @return {Promise<Array>}
 */
var promiseAllSettled = function(functions) {
    return new Promise((resolve) => {
        let results = [];
        let completed = 0;

        functions.forEach((func, index) => {
            func().then(value => {
                results[index] = { status: "fulfilled", value: value };
            }).catch(reason => {
                results[index] = { status: "rejected", reason: reason };
            }).finally(() => {
                completed++;
                if (completed === functions.length) {
                    resolve(results);
                }
            });
        });
    });
};