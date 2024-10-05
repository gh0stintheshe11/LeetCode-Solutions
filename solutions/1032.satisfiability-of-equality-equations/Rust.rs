struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl UnionFind {
    fn new(size: usize) -> Self {
        UnionFind {
            parent: (0..size).collect(),
            rank: vec![0; size],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]);
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let root_x = self.find(x);
        let root_y = self.find(y);
        if root_x != root_y {
            match self.rank[root_x].cmp(&self.rank[root_y]) {
                std::cmp::Ordering::Less => self.parent[root_x] = root_y,
                std::cmp::Ordering::Greater => self.parent[root_y] = root_x,
                std::cmp::Ordering::Equal => {
                    self.parent[root_y] = root_x;
                    self.rank[root_x] += 1;
                }
            }
        }
    }
}

impl Solution {
    pub fn equations_possible(equations: Vec<String>) -> bool {
        let mut uf = UnionFind::new(26); // 26 lowercase letters
        
        // First pass: process all equality equations
        for eq in &equations {
            let chars: Vec<char> = eq.chars().collect();
            if chars[1] == '=' {
                let x = chars[0] as usize - 'a' as usize;
                let y = chars[3] as usize - 'a' as usize;
                uf.union(x, y);
            }
        }
        
        // Second pass: check inequality equations
        for eq in &equations {
            let chars: Vec<char> = eq.chars().collect();
            if chars[1] == '!' {
                let x = chars[0] as usize - 'a' as usize;
                let y = chars[3] as usize - 'a' as usize;
                if uf.find(x) == uf.find(y) {
                    return false; // Contradiction found
                }
            }
        }
        
        true // No contradictions found
    }
}