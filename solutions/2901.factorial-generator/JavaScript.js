/**
 * @param {number} n
 * @yields {number}
 */
function* factorial(n) {
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
        yield result;
    }
    if (n === 0) {
        yield 1;
    }
};