/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    
    return function(...args) {
        let currentCache = cache;
        for (const arg of args) {
            if (!currentCache.has(arg)) {
                currentCache.set(arg, new Map());
            }
            currentCache = currentCache.get(arg);
        }

        if (!currentCache.has('result')) {
            currentCache.set('result', fn(...args));
        }
        
        return currentCache.get('result');
    }
}