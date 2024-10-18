/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
    let activeCount = 0;
    let i = 0;
    
    function next() {
        if (i >= functions.length) return Promise.resolve();
        
        const fn = functions[i++];
        activeCount++;
        
        return fn().then(() => {
            activeCount--;
            return next();
        });
    }
    
    const promises = [];
    for (let j = 0; j < Math.min(n, functions.length); j++) {
        promises.push(next());
    }
    
    return Promise.all(promises);
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */