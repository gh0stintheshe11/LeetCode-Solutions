/**
 * @param {Array<number>} arr
 * @param {number} startIndex
 * @yields {number}
 */
var cycleGenerator = function* (arr, startIndex) {
    let currentIndex = startIndex;
    const n = arr.length;
    while (true) {
        const jump = yield arr[currentIndex];
        if (jump !== undefined) {
            currentIndex = (currentIndex + jump) % n;
            if (currentIndex < 0) currentIndex += n;
        }
    }
};

/**
 *  const gen = cycleGenerator([1,2,3,4,5], 0);
 *  gen.next().value  // 1
 *  gen.next(1).value // 2
 *  gen.next(2).value // 4
 *  gen.next(6).value // 5
 */