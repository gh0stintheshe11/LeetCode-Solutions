/**
 * @param {Object|Array} obj
 * @param {Function} fn
 * @return {Object|Array|undefined}
 */
var deepFilter = function(obj, fn) {
    if (Array.isArray(obj)) {
        let result = [];
        for (let item of obj) {
            if (typeof item !== 'object' || item === null) {
                if (fn(item)) result.push(item);
            } else {
                let filteredChild = deepFilter(item, fn);
                if (filteredChild !== undefined) result.push(filteredChild);
            }
        }
        return result.length > 0 ? result : undefined;
    } else if (typeof obj === 'object' && obj !== null) {
        let result = {};
        for (let key in obj) {
            if (typeof obj[key] !== 'object' || obj[key] === null) {
                if (fn(obj[key])) result[key] = obj[key];
            } else {
                let filteredChild = deepFilter(obj[key], fn);
                if (filteredChild !== undefined) result[key] = filteredChild;
            }
        }
        return Object.keys(result).length > 0 ? result : undefined;
    }
    return undefined;
};