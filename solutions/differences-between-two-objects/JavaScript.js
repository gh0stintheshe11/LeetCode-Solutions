/**
 * @param {Object|Array} obj1
 * @param {Object|Array} obj2
 * @return {Object|Array}
 */
function objDiff(obj1, obj2) {
  if (obj1 === obj2) return {};

  if (
    (obj1 === null || obj2 === null)
    || (typeof obj1 !== 'object' || typeof obj2 !== 'object')
    || (Array.isArray(obj1) !== Array.isArray(obj2))
  ) return [obj1, obj2];

  const diff = {};

  for (const key in obj1) {
    if (key in obj2) {
      const valueDiff = objDiff(obj1[key], obj2[key]);

      if (Object.keys(valueDiff).length) diff[key] = valueDiff;
    }
  }

  return diff;
};