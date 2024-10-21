/**
 * @param {Function} fn
 * @return {Function<Promise<number>>}
 */
var promisify = function(fn) {
    return function(...args) {
        return new Promise((resolve, reject) => {
            fn((result, error) => {
                if (error !== undefined) {
                    reject(error);
                } else {
                    resolve(result);
                }
            }, ...args);
        });
    }
};

/**
 * const asyncFunc = promisify(callback => callback(42));
 * asyncFunc().then(console.log); // 42
 */