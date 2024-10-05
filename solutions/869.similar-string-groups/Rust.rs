impl Solution {
    pub fn num_similar_groups(strs: Vec<String>) -> i32 {
        let n = strs.len();
        let mut parent: Vec<usize> = (0..n).collect();
        let mut rank: Vec<usize> = vec![0; n];
        
        fn find(parent: &mut Vec<usize>, x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        
        fn union(parent: &mut Vec<usize>, rank: &mut Vec<usize>, x: usize, y: usize) {
            let root_x = find(parent, x);
            let root_y = find(parent, y);
            if root_x != root_y {
                if rank[root_x] < rank[root_y] {
                    parent[root_x] = root_y;
                } else if rank[root_x] > rank[root_y] {
                    parent[root_y] = root_x;
                } else {
                    parent[root_y] = root_x;
                    rank[root_x] += 1;
                }
            }
        }
        
        fn is_similar(s1: &str, s2: &str) -> bool {
            let mut diff = 0;
            for (c1, c2) in s1.chars().zip(s2.chars()) {
                if c1 != c2 {
                    diff += 1;
                    if diff > 2 {
                        return false;
                    }
                }
            }
            true
        }
        
        for i in 0..n {
            for j in i+1..n {
                if is_similar(&strs[i], &strs[j]) {
                    union(&mut parent, &mut rank, i, j);
                }
            }
        }
        
        let mut groups = 0;
        for i in 0..n {
            if parent[i] == i {
                groups += 1;
            }
        }
        
        groups
    }
}