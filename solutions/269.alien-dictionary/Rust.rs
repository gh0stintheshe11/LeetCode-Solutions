use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn alien_order(words: Vec<String>) -> String {
        let mut graph: HashMap<char, HashSet<char>> = HashMap::new();
        let mut in_degree: HashMap<char, i32> = HashMap::new();
        
        // Initialize the graph and in_degree
        for word in &words {
            for &c in word.as_bytes() {
                graph.entry(c as char).or_insert(HashSet::new());
                in_degree.entry(c as char).or_insert(0);
            }
        }
        
        // Build the graph
        for i in 0..words.len() - 1 {
            let word1 = &words[i];
            let word2 = &words[i + 1];
            let min_len = word1.len().min(word2.len());
            
            if word1.len() > word2.len() && word1.starts_with(word2) {
                return String::new(); // Invalid order
            }
            
            for j in 0..min_len {
                if word1.as_bytes()[j] != word2.as_bytes()[j] {
                    let c1 = word1.as_bytes()[j] as char;
                    let c2 = word2.as_bytes()[j] as char;
                    if !graph[&c1].contains(&c2) {
                        graph.get_mut(&c1).unwrap().insert(c2);
                        *in_degree.get_mut(&c2).unwrap() += 1;
                    }
                    break;
                }
            }
        }
        
        // Topological sorting
        let mut queue: VecDeque<char> = in_degree.iter()
            .filter(|&(_, &degree)| degree == 0)
            .map(|(&c, _)| c)
            .collect();
        let mut result = String::new();
        
        while let Some(c) = queue.pop_front() {
            result.push(c);
            if let Some(neighbors) = graph.get(&c) {
                for &next in neighbors {
                    *in_degree.get_mut(&next).unwrap() -= 1;
                    if in_degree[&next] == 0 {
                        queue.push_back(next);
                    }
                }
            }
        }
        
        if result.len() == in_degree.len() {
            result
        } else {
            String::new() // Cycle detected
        }
    }
}