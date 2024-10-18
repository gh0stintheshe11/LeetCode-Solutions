use std::collections::HashMap;

impl Solution {
    pub fn num_of_minutes(n: i32, head_id: i32, manager: Vec<i32>, inform_time: Vec<i32>) -> i32 {
        let mut subordinates: HashMap<i32, Vec<i32>> = HashMap::new();
        
        // Build the hierarchy
        for (i, &m) in manager.iter().enumerate() {
            if m != -1 {
                subordinates.entry(m).or_insert(Vec::new()).push(i as i32);
            }
        }
        
        // DFS function to calculate time
        fn dfs(employee: i32, subordinates: &HashMap<i32, Vec<i32>>, inform_time: &Vec<i32>) -> i32 {
            match subordinates.get(&employee) {
                Some(subs) => {
                    let max_sub_time = subs.iter()
                        .map(|&sub| dfs(sub, subordinates, inform_time))
                        .max()
                        .unwrap_or(0);
                    inform_time[employee as usize] + max_sub_time
                },
                None => 0
            }
        }
        
        dfs(head_id, &subordinates, &inform_time)
    }
}