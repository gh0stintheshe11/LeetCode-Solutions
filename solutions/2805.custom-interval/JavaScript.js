let intervalCount = 0;
const intervalMap = new Map();

function customInterval(fn, delay, period) {
    let count = 0;
    const executeFunction = () => {
        fn();
        count++;
        const nextInterval = delay + period * count;
        intervalMap.set(id, setTimeout(executeFunction, nextInterval));
    };
    const id = intervalCount++;
    intervalMap.set(id, setTimeout(executeFunction, delay));
    return id;
}

function customClearInterval(id) {
    clearTimeout(intervalMap.get(id));
    intervalMap.delete(id);
}