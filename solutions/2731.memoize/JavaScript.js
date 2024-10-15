/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    let callCount = 0;

    function stringifyArgs(args) {
        return JSON.stringify(args);
    }

    return function (...args) {
        const key = stringifyArgs(args);
        if (!cache.has(key)) {
            cache.set(key, fn(...args));
            callCount += 1;
        }
        return cache.get(key);
    }
}