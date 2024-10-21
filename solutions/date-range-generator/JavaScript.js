/**
 * @param {string} start
 * @param {string} end
 * @param {number} step
 * @yields {string}
 */
var dateRangeGenerator = function* (start, end, step) {
    const startDate = new Date(start);
    const endDate = new Date(end);
    const millisInADay = 24 * 60 * 60 * 1000;
    
    for (let currentDate = startDate; currentDate <= endDate; currentDate = new Date(currentDate.getTime() + step * millisInADay)) {
        yield currentDate.toISOString().split('T')[0];
    }
};

/**
 * const g = dateRangeGenerator('2023-04-01', '2023-04-04', 1);
 * g.next().value; // '2023-04-01'
 * g.next().value; // '2023-04-02'
 * g.next().value; // '2023-04-03'
 * g.next().value; // '2023-04-04'
 * g.next().done; // true
 */