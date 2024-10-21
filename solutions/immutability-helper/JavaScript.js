var ImmutableHelper = function(obj) {
    this.original = obj;
    this.mutated = false;

    this.getPartialClone = (ori, cur) => {
        const setTrap = (target, prop, value) => {
            if (target[prop] !== value) {
                cur[prop] = value;
                this.mutated = true;
            }
        }
        const getTrap = (target, prop) => {
            if (target[prop] !== null && typeof target[prop] === 'object') {
                if (cur[prop] === undefined) {
                    cur[prop] = {};
                }
                return this.getPartialClone(target[prop], cur[prop]);
            }
            return cur[prop] === undefined ? Reflect.get(target, prop) : cur[prop];
        }

        return new Proxy(
            ori, {set: setTrap.bind(this), get: getTrap.bind(this)},
        );
    }
    
    this.clone = (ori, pc) => {
        if (ori === null || typeof ori !== 'object' || typeof pc !== 'object')
		    return pc;
        let res;
        if (Array.isArray(ori)) {
            res = [...ori];
            for (let [k, v] of Object.entries(pc)) {
                const idx = parseInt(k, 10);
                res[idx] = this.clone(ori[idx], v);
            }
        } else {
            res = {...ori};
            for (let [k, v] of Object.entries(pc)) {
                res[k] = this.clone(ori[k], v);
            }
        }
        return res;
    }
};

/** 
 * @param {Function} mutator
 * @return {JSON} clone of obj
 */
ImmutableHelper.prototype.produce = function(mutator) {
    const pc = {};
    mutator(this.getPartialClone(this.original, pc));
	if (this.mutated) {
    	this.mutated = false;
	    return this.clone(this.original, pc)
	}
    return this.original;
};