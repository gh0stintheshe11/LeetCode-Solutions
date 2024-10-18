/**
 * @param {Function} fn
 * @param {Array} args
 * @return {Function}
 */
var partial = function(fn, args) {
    return function(...restArgs) {
        let modifiedArgs = [];
        let restIndex = 0;
        
        for (let i = 0; i < args.length; i++) {
            if (args[i] === '_') {
                modifiedArgs.push(restArgs[restIndex]);
                restIndex++;
            } else {
                modifiedArgs.push(args[i]);
            }
        }
        
        modifiedArgs.push(...restArgs.slice(restIndex));
        
        return fn(...modifiedArgs);
    }
};