var TimeLimitedCache = function() {
    this.cache = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    if (this.cache.has(key)) {
        clearTimeout(this.cache.get(key).timeoutId);
        this.cache.delete(key);
        var existed = true;
    } else {
        var existed = false;
    }

    const expireTime = Date.now() + duration;
    const timeoutId = setTimeout(() => {
        this.cache.delete(key);
    }, duration);

    this.cache.set(key, { value, expireTime, timeoutId });
    return existed;
};

TimeLimitedCache.prototype.get = function(key) {
    if (!this.cache.has(key)) {
        return -1;
    }

    const { value, expireTime } = this.cache.get(key);
    if (Date.now() > expireTime) {
        this.cache.delete(key);
        return -1;
    }
    return value;
};

TimeLimitedCache.prototype.count = function() {
    let count = 0;
    const now = Date.now();

    for (const [key, { expireTime }] of this.cache.entries()) {
        if (now <= expireTime) {
            count++;
        } else {
            this.cache.delete(key);
        }
    }

    return count;
};