impl Solution {
    pub fn valid_tree(n: i32, edges: Vec<Vec<i32>>) -> bool {
        if edges.len() != n as usize - 1 {
            return false;
        }

        let mut parent: Vec<i32> = (0..n).collect();

        fn find(parent: &mut Vec<i32>, i: i32) -> i32 {
            if parent[i as usize] != i {
                parent[i as usize] = find(parent, parent[i as usize]);
            }
            parent[i as usize]
        }

        for edge in edges {
            let root1 = find(&mut parent, edge[0]);
            let root2 = find(&mut parent, edge[1]);
            
            if root1 == root2 {
                return false;
            }
            
            parent[root1 as usize] = root2;
        }

        true
    }
}