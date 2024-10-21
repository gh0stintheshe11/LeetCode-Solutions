use std::collections::HashMap;

impl Solution {
    pub fn longest_str_chain(words: Vec<String>) -> i32 {
        // Sort words by their lengths
        let mut words = words;
        words.sort_by_key(|word| word.len());
        
        // HashMap to store the longest chain length ending at each word
        let mut dp: HashMap<String, i32> = HashMap::new();
        let mut max_chain_length = 1;
        
        for word in words {
            let mut current_length = 1;
            
            // Try removing each character from the word
            for i in 0..word.len() {
                let mut predecessor = word.clone();
                predecessor.remove(i);
                
                if let Some(&length) = dp.get(&predecessor) {
                    current_length = current_length.max(length + 1);
                }
            }
            
            dp.insert(word, current_length);
            max_chain_length = max_chain_length.max(current_length);
        }
        
        max_chain_length
    }
}
