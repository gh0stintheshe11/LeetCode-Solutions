/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj.reduce((acc, el) => {
            const compactedElement = compactObject(el);
            if (Boolean(compactedElement)) {
                acc.push(compactedElement);
            }
            return acc;
        }, []);
    } else if (typeof obj === 'object' && obj !== null) {
        return Object.entries(obj).reduce((acc, [key, value]) => {
            const compactedValue = compactObject(value);
            if (Boolean(compactedValue)) {
                acc[key] = compactedValue;
            }
            return acc;
        }, {});
    }
    return obj;
};