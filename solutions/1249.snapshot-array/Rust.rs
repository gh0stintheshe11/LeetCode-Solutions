use std::collections::HashMap;

struct SnapshotArray {
    data: Vec<HashMap<i32, i32>>,
    snap_id: i32,
}

impl SnapshotArray {
    fn new(length: i32) -> Self {
        let mut data = Vec::with_capacity(length as usize);
        for _ in 0..length {
            data.push(HashMap::new());
        }
        SnapshotArray {
            data,
            snap_id: 0,
        }
    }

    fn set(&mut self, index: i32, val: i32) {
        self.data[index as usize].insert(self.snap_id, val);
    }

    fn snap(&mut self) -> i32 {
        let current_snap_id = self.snap_id;
        self.snap_id += 1;
        current_snap_id
    }

    fn get(&self, index: i32, snap_id: i32) -> i32 {
        let mut snap_id = snap_id;
        while snap_id >= 0 {
            if let Some(&val) = self.data[index as usize].get(&snap_id) {
                return val;
            }
            snap_id -= 1;
        }
        0
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */
