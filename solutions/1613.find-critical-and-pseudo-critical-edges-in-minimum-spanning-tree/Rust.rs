use std::collections::HashSet;

struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            parent: (0..n).collect(),
            rank: vec![0; n],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]);
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) -> bool {
        let root_x = self.find(x);
        let root_y = self.find(y);
        if root_x == root_y {
            return false;
        }
        match self.rank[root_x].cmp(&self.rank[root_y]) {
            std::cmp::Ordering::Less => self.parent[root_x] = root_y,
            std::cmp::Ordering::Greater => self.parent[root_y] = root_x,
            std::cmp::Ordering::Equal => {
                self.parent[root_y] = root_x;
                self.rank[root_x] += 1;
            }
        }
        true
    }
}

impl Solution {
    pub fn find_critical_and_pseudo_critical_edges(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut edges: Vec<_> = edges.into_iter().enumerate().collect();
        edges.sort_by_key(|&(_, ref e)| e[2]);

        let mst_weight = Self::kruskal(n, &edges, None, None);

        let mut critical = Vec::new();
        let mut pseudo_critical = Vec::new();

        for i in 0..edges.len() {
            // Check if the edge is critical
            if Self::kruskal(n, &edges, Some(i), None) > mst_weight {
                critical.push(edges[i].0 as i32);
            } else if Self::kruskal(n, &edges, None, Some(i)) == mst_weight {
                pseudo_critical.push(edges[i].0 as i32);
            }
        }

        vec![critical, pseudo_critical]
    }

    fn kruskal(n: usize, edges: &[(usize, Vec<i32>)], skip: Option<usize>, force: Option<usize>) -> i32 {
        let mut uf = UnionFind::new(n);
        let mut weight = 0;
        let mut count = 0;

        if let Some(f) = force {
            let (u, v, w) = (edges[f].1[0] as usize, edges[f].1[1] as usize, edges[f].1[2]);
            uf.union(u, v);
            weight += w;
            count += 1;
        }

        for (i, edge) in edges.iter().enumerate() {
            if Some(i) == skip {
                continue;
            }
            let (u, v, w) = (edge.1[0] as usize, edge.1[1] as usize, edge.1[2]);
            if uf.union(u, v) {
                weight += w;
                count += 1;
                if count == n - 1 {
                    break;
                }
            }
        }

        if count == n - 1 { weight } else { i32::MAX }
    }
}