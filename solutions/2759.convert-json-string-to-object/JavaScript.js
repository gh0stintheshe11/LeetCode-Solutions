/**
 * @param {string} str
 * @return {null|boolean|number|string|Array|Object}
 */
var jsonParse = function(str) {
    let index = 0;
    
    function parseValue() {
        switch (str[index]) {
            case '{':
                return parseObject();
            case '[':
                return parseArray();
            case '"':
                return parseString();
            case 't':
            case 'f':
                return parseBoolean();
            case 'n':
                return parseNull();
            default:
                return parseNumber();
        }
    };
    
    function parseObject() {
        let obj = {};
        index++; // skip '{'
        while (str[index] !== '}') {
            if (str[index] === ',') {
                index++; // skip ','
            }
            let key = parseString();
            index++; // skip ':'
            let value = parseValue();
            obj[key] = value;
        }
        index++; // skip '}'
        return obj;
    }
    
    function parseArray() {
        let arr = [];
        index++; // skip '['
        while (str[index] !== ']') {
            if (str[index] === ',') {
                index++; // skip ','
            }
            arr.push(parseValue());
        }
        index++; // skip ']'
        return arr;
    }
    
    function parseString() {
        let result = '';
        index++; // skip '"'
        while (str[index] !== '"') {
            result += str[index++];
        }
        index++; // skip '"'
        return result;
    }
    
    function parseBoolean() {
        if (str.substring(index, index + 4) === 'true') {
            index += 4;
            return true;
        } else {
            index += 5;
            return false;
        }
    }
    
    function parseNull() {
        index += 4; // skip 'null'
        return null;
    }
    
    function parseNumber() {
        let numStr = '';
        while (str[index] >= '0' && str[index] <= '9' || str[index] === '-' || str[index] === '.') {
            numStr += str[index++];
        }
        return parseFloat(numStr);
    }
    
    return parseValue();
};