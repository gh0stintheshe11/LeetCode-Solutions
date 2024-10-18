use std::collections::HashMap;

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        // Split the sentences into words
        let words1 = s1.split_whitespace();
        let words2 = s2.split_whitespace();
        
        // Create a hash map to count occurrences of each word
        let mut word_count = HashMap::new();
        
        // Count words in the first sentence
        for word in words1 {
            *word_count.entry(word).or_insert(0) += 1;
        }
        
        // Count words in the second sentence
        for word in words2 {
            *word_count.entry(word).or_insert(0) += 1;
        }
        
        // Collect words that appear exactly once
        let mut uncommon_words = Vec::new();
        for (word, count) in word_count {
            if count == 1 {
                uncommon_words.push(word.to_string());
            }
        }
        
        uncommon_words
    }
}
