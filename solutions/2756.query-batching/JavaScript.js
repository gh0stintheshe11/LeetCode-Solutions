var QueryBatcher = function(queryMultiple, t) {
    this.queryMultiple = queryMultiple;
    this.t = t;
    this.keyResolve = [];
    this.waiting = false;
};

QueryBatcher.prototype.getValue = async function(key) {
    let retPromise;
    if (key !== undefined) {
        retPromise = new Promise((resolve) => this.keyResolve.push({key, resolve}));
    }
    if (!this.waiting && this.keyResolve.length > 0) {
        const localKeyResolve = this.keyResolve;
        this.waiting = true;
        this.keyResolve = [];
        setTimeout(() => {
            this.waiting = false;
            this.getValue();
        }, this.t);

        const resList = await this.queryMultiple(localKeyResolve.map(it => it.key));
        for (let i in resList) {
            localKeyResolve[i].resolve(resList[i]);
        }
    }
    return retPromise;
};