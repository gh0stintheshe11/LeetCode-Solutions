/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    fn(...args); // Invoke immediately
    const interval = setInterval(() => fn(...args), t);
    return () => clearInterval(interval);
};