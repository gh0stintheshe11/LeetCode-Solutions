/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let idMap = new Map();

    for (let obj of arr1) {
        idMap.set(obj.id, obj);
    }

    for (let obj of arr2) {
        if (idMap.has(obj.id)) {
            let mergedObj = { ...idMap.get(obj.id), ...obj };
            idMap.set(obj.id, mergedObj);
        } else {
            idMap.set(obj.id, obj);
        }
    }
    
    return Array.from(idMap.values()).sort((a, b) => a.id - b.id);
};