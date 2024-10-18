use std::collections::HashMap;

struct TimeMap {
    store: HashMap<String, Vec<(i32, String)>>,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            store: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.store.entry(key).or_insert(Vec::new()).push((timestamp, value));
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        if let Some(entries) = self.store.get(&key) {
            let mut left = 0;
            let mut right = entries.len() as i32 - 1;
            while left <= right {
                let mid = left + (right - left) / 2;
                if entries[mid as usize].0 <= timestamp {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            if right >= 0 {
                return entries[right as usize].1.clone();
            }
        }
        "".to_string()
    }
}