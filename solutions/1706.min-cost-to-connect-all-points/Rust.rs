use std::collections::BinaryHeap;
use std::cmp::Reverse;

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
    pub fn min_cost_connect_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut edges = BinaryHeap::new();

        // Calculate distances between all pairs of points
        for i in 0..n {
            for j in i+1..n {
                let distance = (points[i][0] - points[j][0]).abs() + (points[i][1] - points[j][1]).abs();
                edges.push(Reverse((distance, i, j)));
            }
        }

        let mut uf = UnionFind::new(n);
        let mut total_cost = 0;
        let mut edges_used = 0;

        // Kruskal's algorithm
        while let Some(Reverse((cost, x, y))) = edges.pop() {
            if uf.union(x, y) {
                total_cost += cost;
                edges_used += 1;
                if edges_used == n - 1 {
                    break;
                }
            }
        }

        total_cost
    }
}