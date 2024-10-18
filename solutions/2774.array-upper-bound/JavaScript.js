/**
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function(target) {
    let low = 0;
    let high = this.length - 1;
    let result = -1;

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (this[mid] <= target) {
            if (this[mid] === target) {
                result = mid;
            }
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return result;
};