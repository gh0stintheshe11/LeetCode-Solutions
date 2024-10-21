/** 
 * @return {string}
 */
Date.prototype.nextDay = function() {
    this.setDate(this.getDate() + 1);
    let year = this.getFullYear();
    let month = String(this.getMonth() + 1).padStart(2, '0');
    let day = String(this.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */