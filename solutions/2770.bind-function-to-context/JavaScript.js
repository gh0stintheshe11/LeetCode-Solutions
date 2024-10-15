Function.prototype.bindPolyfill = function(obj) {
    const fn = this;
    return function(...args) {
        return fn.apply(obj, args);
    };
}