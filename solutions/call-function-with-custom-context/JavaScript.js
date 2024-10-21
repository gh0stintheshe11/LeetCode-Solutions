Function.prototype.callPolyfill = function(context, ...args) {
    context = context || globalThis;
    const uniqueKey = Symbol('fnKey');
    context[uniqueKey] = this;
    const result = context[uniqueKey](...args);
    delete context[uniqueKey];
    return result;
}