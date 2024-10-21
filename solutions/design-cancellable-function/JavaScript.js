function cancellable(generator) {
    let cancel

    const promise = new Promise((resolve, reject) => {
        function step(val, err, isCancel) {
            try {
                const { value, done } = err ? generator.throw(err) : generator.next(val)
                if (done || isCancel) resolve(value)
                else value.then(step, e => step(undefined, e))
            } catch (e) {
                reject(e)
            }
        }
        cancel = () => step(undefined, "Cancelled", true)
        step()
    })

    return [cancel, promise]
};