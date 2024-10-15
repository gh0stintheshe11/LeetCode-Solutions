/**
 * @param {Object|Array} obj
 * @return {Object}
 */
var invertObject = function(obj) {
    const invertedObj = {};
    for (const key in obj) {
        const value = obj[key];
        if (invertedObj.hasOwnProperty(value)) {
            if (Array.isArray(invertedObj[value])) {
                invertedObj[value].push(key);
            } else {
                invertedObj[value] = [invertedObj[value], key];
            }
        } else {
            invertedObj[value] = key;
        }
    }
    return invertedObj;
};