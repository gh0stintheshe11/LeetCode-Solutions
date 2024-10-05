use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn min_mutation(start_gene: String, end_gene: String, bank: Vec<String>) -> i32 {
        let mut bank_set: HashSet<String> = bank.into_iter().collect();
        let mut queue = VecDeque::new();
        let mut visited = HashSet::new();
        let genes = ['A', 'C', 'G', 'T'];

        queue.push_back((start_gene.clone(), 0));
        visited.insert(start_gene);

        while let Some((current_gene, mutations)) = queue.pop_front() {
            if current_gene == end_gene {
                return mutations;
            }

            for i in 0..8 {
                let mut gene_chars: Vec<char> = current_gene.chars().collect();
                for &gene in &genes {
                    if gene_chars[i] != gene {
                        gene_chars[i] = gene;
                        let new_gene: String = gene_chars.iter().collect();
                        if bank_set.contains(&new_gene) && !visited.contains(&new_gene) {
                            queue.push_back((new_gene.clone(), mutations + 1));
                            visited.insert(new_gene);
                        }
                    }
                }
            }
        }

        -1
    }
}