use std::collections::HashMap;
use std::cmp::min;

impl Solution {
    pub fn make_array_increasing(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut arr2 = arr2;
        arr2.sort_unstable();
        arr2.dedup();
        
        let n1 = arr1.len();
        let mut dp: HashMap<(usize, i32), i32> = HashMap::new();
        
        let result = Self::dfs(0, -1, &arr1, &arr2, &mut dp);
        if result > n1 as i32 {
            -1
        } else {
            result
        }
    }
    
    fn dfs(i: usize, prev: i32, arr1: &Vec<i32>, arr2: &Vec<i32>, dp: &mut HashMap<(usize, i32), i32>) -> i32 {
        if i == arr1.len() {
            return 0;
        }
        
        if let Some(&result) = dp.get(&(i, prev)) {
            return result;
        }
        
        let mut result = arr1.len() as i32 + 1;
        
        // Keep arr1[i] if it's greater than prev
        if arr1[i] > prev {
            result = min(result, Self::dfs(i + 1, arr1[i], arr1, arr2, dp));
        }
        
        // Replace arr1[i] with the smallest element from arr2 that is greater than prev
        if let Ok(j) = arr2.binary_search(&(prev + 1)) {
            result = min(result, 1 + Self::dfs(i + 1, arr2[j], arr1, arr2, dp));
        } else if let Err(j) = arr2.binary_search(&(prev + 1)) {
            if j < arr2.len() {
                result = min(result, 1 + Self::dfs(i + 1, arr2[j], arr1, arr2, dp));
            }
        }
        
        dp.insert((i, prev), result);
        result
    }
}