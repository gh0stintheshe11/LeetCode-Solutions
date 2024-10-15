/**
 * @param {Array} arr
 * @param {number} n
 * @return {Array}
 */
var flat = function (arr, n) {
    const result = [];
    
    function flatten(currentArray, currentDepth) {
        for (let item of currentArray) {
            if (Array.isArray(item) && currentDepth < n) {
                flatten(item, currentDepth + 1);
            } else {
                result.push(item);
            }
        }
    }
    
    flatten(arr, 0);
    return result;
};