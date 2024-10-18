/**
 * @param {number} times
 * @return {string}
 */
String.prototype.replicate = function(times) {
    let result = '';
    let base = this.toString();
    while (times > 0) {
        if (times % 2 === 1) {
            result += base;
        }
        base += base;
        times = Math.floor(times / 2);
    }
    return result;
}