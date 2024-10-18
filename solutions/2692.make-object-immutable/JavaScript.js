/**
 * @param {Object|Array} obj
 * @return {Object|Array} immutable obj
 */
var makeImmutable = function(obj) {
    const mutableMethods = ['pop', 'push', 'shift', 'unshift', 'splice', 'sort', 'reverse'];

    const handler = {
        set(target, prop, value) {
            if (Array.isArray(target)) {
                throw `Error Modifying Index: ${prop}`;
            } else {
                throw `Error Modifying: ${prop}`;
            }
        },
        get(target, prop, receiver) {
            const original = Reflect.get(target, prop, receiver);

            if (typeof original === 'function' && mutableMethods.includes(prop)) {
                return function() {
                    throw `Error Calling Method: ${prop}`;
                };
            }

            if (original && typeof original === 'object') {
                return new Proxy(original, handler);
            }

            return original;
        }
    };

    return new Proxy(obj, handler);
};

/**
 * const obj = makeImmutable({x: 5});
 * obj.x = 6; // throws "Error Modifying x"
 */