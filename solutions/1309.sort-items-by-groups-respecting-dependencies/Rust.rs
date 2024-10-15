use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn sort_items(n: i32, m: i32, group: Vec<i32>, before_items: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut m = m as usize;
        
        // Assign a unique group to items with no group
        let mut group = group;
        for i in 0..n {
            if group[i] == -1 {
                group[i] = m as i32;
                m += 1;
            }
        }
        
        // Build group and item graphs
        let mut group_graph = vec![HashSet::new(); m];
        let mut item_graph = vec![HashSet::new(); n];
        let mut group_indegree = vec![0; m];
        let mut item_indegree = vec![0; n];
        
        for (i, before) in before_items.iter().enumerate() {
            for &j in before {
                let j = j as usize;
                if group[i] != group[j] {
                    if group_graph[group[j] as usize].insert(group[i] as usize) {
                        group_indegree[group[i] as usize] += 1;
                    }
                }
                if item_graph[j].insert(i) {
                    item_indegree[i] += 1;
                }
            }
        }
        
        // Topological sort for groups
        let group_order = Self::topological_sort(&group_graph, &mut group_indegree);
        if group_order.is_empty() {
            return vec![];
        }
        
        // Topological sort for items
        let item_order = Self::topological_sort(&item_graph, &mut item_indegree);
        if item_order.is_empty() {
            return vec![];
        }
        
        // Combine the results
        let mut group_items: HashMap<usize, Vec<usize>> = HashMap::new();
        for &item in &item_order {
            group_items.entry(group[item] as usize).or_default().push(item);
        }
        
        let mut result = Vec::new();
        for &g in &group_order {
            if let Some(items) = group_items.get(&g) {
                result.extend(items.iter().map(|&x| x as i32));
            }
        }
        
        result
    }
    
    fn topological_sort(graph: &[HashSet<usize>], indegree: &mut [i32]) -> Vec<usize> {
        let n = graph.len();
        let mut queue = VecDeque::new();
        for i in 0..n {
            if indegree[i] == 0 {
                queue.push_back(i);
            }
        }
        
        let mut order = Vec::new();
        while let Some(node) = queue.pop_front() {
            order.push(node);
            for &neighbor in &graph[node] {
                indegree[neighbor] -= 1;
                if indegree[neighbor] == 0 {
                    queue.push_back(neighbor);
                }
            }
        }
        
        if order.len() == n { order } else { Vec::new() }
    }
}