/**
 * @param {null|boolean|number|string|Array|Object} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) {
        return "null";
    } else if (typeof object === "string") {
        return `"${object}"`;
    } else if (typeof object === "number" || typeof object === "boolean") {
        return String(object);
    } else if (Array.isArray(object)) {
        const arr = object.map(item => jsonStringify(item));
        return `[${arr.join(",")}]`;
    } else if (typeof object === "object") {
        const keys = Object.keys(object);
        const objString = keys.map(key => `"${key}":${jsonStringify(object[key])}`);
        return `{${objString.join(",")}}`;
    }
};