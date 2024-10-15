use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        let mut word_set: HashSet<String> = word_list.into_iter().collect();
        
        // If end_word is not in the word_set, no transformation sequence exists
        if !word_set.contains(&end_word) {
            return 0;
        }
        
        let mut queue = VecDeque::new();
        queue.push_back((begin_word.clone(), 1));
        
        let mut visited = HashSet::new();
        visited.insert(begin_word);
        
        while let Some((word, level)) = queue.pop_front() {
            if word == end_word {
                return level;
            }
            
            for i in 0..word.len() {
                let mut chars: Vec<char> = word.chars().collect();
                for c in 'a'..='z' {
                    chars[i] = c;
                    let new_word: String = chars.iter().collect();
                    
                    if word_set.contains(&new_word) && !visited.contains(&new_word) {
                        queue.push_back((new_word.clone(), level + 1));
                        visited.insert(new_word);
                    }
                }
            }
        }
        
        0
    }
}