/**
 * @param {null|boolean|number|string|Array|Object} obj1
 * @param {null|boolean|number|string|Array|Object} obj2
 * @return {null|boolean|number|string|Array|Object}
 */
var deepMerge = function(obj1, obj2) {
    if (typeof obj1 === 'object' && obj1 !== null && typeof obj2 === 'object' && obj2 !== null) {
        if (Array.isArray(obj1) && Array.isArray(obj2)) {
            const result = [];
            const maxLength = Math.max(obj1.length, obj2.length);
            for (let i = 0; i < maxLength; i++) {
                if (i < obj1.length && i < obj2.length) {
                    result[i] = deepMerge(obj1[i], obj2[i]);
                } else if (i < obj1.length) {
                    result[i] = obj1[i];
                } else {
                    result[i] = obj2[i];
                }
            }
            return result;
        } else if (!Array.isArray(obj1) && !Array.isArray(obj2)) {
            const result = {};
            const keys = new Set([...Object.keys(obj1), ...Object.keys(obj2)]);
            for (let key of keys) {
                if (key in obj1 && key in obj2) {
                    result[key] = deepMerge(obj1[key], obj2[key]);
                } else if (key in obj1) {
                    result[key] = obj1[key];
                } else {
                    result[key] = obj2[key];
                }
            }
            return result;
        } else {
            return obj2;
        }
    } else {
        return obj2;
    }
};