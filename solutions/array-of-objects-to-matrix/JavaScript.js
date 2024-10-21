/**
 * @param {Array} arr
 * @return {(string | number | boolean | null)[][]}
 */
var jsonToMatrix = function(arr) {
  const result = {};
  const resultArray = [];

  function getKey(currentParentKey, key) {
    return currentParentKey ? `${currentParentKey}.${key}` : key;
  }

  function manageObjectParsing(object, index, currentParentKey = "") {
    const keys = Object.keys(object);
    for (let key of keys) {
      const value = object[key];
      const isObjectType = value !== null && typeof value === "object";
      if (isObjectType) {
        const parentKey = getKey(currentParentKey, key);
        manageObjectParsing(value, index, parentKey);
      } else {
        const columnKey = currentParentKey ? `${currentParentKey}.${key}` : key;
        const row = result[columnKey] ?? [];
        row[index] = value;
        result[columnKey] = row;
      }
    }
  }

  function jsonToMatrixParser() {
    for (let i = 0; i < arr.length; i++) {
      manageObjectParsing(arr[i], i);
    }
  }

  function structureOutput() {
    const colKeys = Object.keys(result).sort((a, b) => a.localeCompare(b));
    resultArray.push(colKeys);
    for (let i = 0; i < arr.length; i++) {
      const row = [];
      for (let columnKey of colKeys) {
        const isValue = result?.[columnKey]?.[i] !== undefined;
        const value = isValue ? result?.[columnKey]?.[i] : "";
        row.push(value);
      }
      resultArray.push(row);
    }
  }

  jsonToMatrixParser();
  structureOutput();
  return resultArray;
};