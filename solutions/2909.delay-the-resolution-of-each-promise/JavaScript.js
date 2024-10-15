/**
 * @param {Array<Function>} functions
 * @param {number} ms
 * @return {Array<Function>}
 */
var delayAll = function(functions, ms) {
    return functions.map(fn => () => 
        new Promise((resolve, reject) => {
            fn()
                .then(value => setTimeout(() => resolve(value), ms))
                .catch(err => setTimeout(() => reject(err), ms));
        })
    );
};