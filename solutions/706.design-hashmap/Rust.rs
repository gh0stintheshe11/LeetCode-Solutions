struct MyHashMap {
    buckets: Vec<Vec<(i32, i32)>>,
    size: usize,
}

impl MyHashMap {
    /** Initialize your data structure here. */
    fn new() -> Self {
        let size = 1000; // Choosing a size for the hash table
        MyHashMap {
            buckets: vec![Vec::new(); size],
            size,
        }
    }

    /** Hash function to compute the index for a given key */
    fn hash(&self, key: i32) -> usize {
        (key as usize) % self.size
    }

    /** Insert a (key, value) pair into the HashMap. If the key already exists, update the corresponding value. */
    fn put(&mut self, key: i32, value: i32) {
        let index = self.hash(key);
        for &mut (ref k, ref mut v) in &mut self.buckets[index] {
            if *k == key {
                *v = value;
                return;
            }
        }
        self.buckets[index].push((key, value));
    }

    /** Return the value to which the specified key is mapped, or -1 if this map contains no mapping for the key. */
    fn get(&self, key: i32) -> i32 {
        let index = self.hash(key);
        for &(k, v) in &self.buckets[index] {
            if k == key {
                return v;
            }
        }
        -1
    }

    /** Remove the mapping for the specified key if this map contains the mapping for the key. */
    fn remove(&mut self, key: i32) {
        let index = self.hash(key);
        if let Some(pos) = self.buckets[index].iter().position(|&(k, _)| k == key) {
            self.buckets[index].remove(pos);
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap::new();
 * obj.put(key, value);
 * let ret_2: i32 = obj.get(key);
 * obj.remove(key);
 */
