/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
    let timeout = null;
    let currArguments = null;

    const execute = () => {
        if (currArguments !== null) {
            fn(...currArguments);
            currArguments = null;
            timeout = setTimeout(execute, t);
        } else {
            clearTimeout(timeout);
            timeout = null;
        }
    };
    
    return function(...args) {
        if (timeout === null) {
            fn(...args);
            timeout = setTimeout(execute, t);
        } else {
            currArguments = args;
        }
    }
};