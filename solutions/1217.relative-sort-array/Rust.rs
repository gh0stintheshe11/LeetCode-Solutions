use std::collections::HashMap;

impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        // Create a hashmap to store the order of elements in arr2
        let mut order_map = HashMap::new();
        for (index, &value) in arr2.iter().enumerate() {
            order_map.insert(value, index);
        }

        // Sort arr1 using a custom comparator
        let mut arr1_sorted = arr1.clone();
        arr1_sorted.sort_by(|a, b| {
            match (order_map.get(a), order_map.get(b)) {
                (Some(&index_a), Some(&index_b)) => index_a.cmp(&index_b),
                (Some(_), None) => std::cmp::Ordering::Less,
                (None, Some(_)) => std::cmp::Ordering::Greater,
                (None, None) => a.cmp(b),
            }
        });

        arr1_sorted
    }
}