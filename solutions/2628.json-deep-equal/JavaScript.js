var areDeeplyEqual = function(o1, o2) {
    if (Array.isArray(o1) !== Array.isArray(o2)) {
        return false;
    }

    if (typeof o1 !== "object" || typeof o2 !== "object" || o1 === null || o2 === null) {
        return o1 === o2;
    }
  
    const o1Keys = Object.keys(o1);
    const o2Keys = Object.keys(o2);
    if (o1Keys.length !== o2Keys.length || !o1Keys.every(key => o2.hasOwnProperty(key))) {
        return false;
    }
  
    return o1Keys.every(key => areDeeplyEqual(o1[key], o2[key]));
};