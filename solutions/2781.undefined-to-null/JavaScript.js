/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var undefinedToNull = function(obj) {
    if (typeof obj !== 'object' || obj === null) return obj;
    
    if (Array.isArray(obj)) {
        return obj.map(undefinedToNull);
    }
    
    const result = {};
    for (const key in obj) {
        result[key] = obj[key] === undefined ? null : undefinedToNull(obj[key]);
    }
    return result;
};