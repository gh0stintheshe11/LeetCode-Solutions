struct UnionFind {
    parent: Vec<usize>,
}

impl UnionFind {
    fn new(size: usize) -> Self {
        UnionFind {
            parent: (0..size).collect(),
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
        if root_x < root_y {
            self.parent[root_y] = root_x;
        } else {
            self.parent[root_x] = root_y;
        }
    }
}

impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        let mut uf = UnionFind::new(26);
        
        // Build the graph
        for (c1, c2) in s1.chars().zip(s2.chars()) {
            uf.union(c1 as usize - 'a' as usize, c2 as usize - 'a' as usize);
        }
        
        // Convert baseStr
        base_str.chars().map(|c| {
            let index = c as usize - 'a' as usize;
            let smallest = uf.find(index) as u8 + b'a';
            smallest as char
        }).collect()
    }
}