use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
    components: usize,
}

impl UnionFind {
    fn new(size: usize) -> Self {
        UnionFind {
            parent: (0..size).collect(),
            rank: vec![0; size],
            components: size,
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
        self.components -= 1;
        true
    }
}

impl Solution {
    pub fn minimum_cost(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut edges = BinaryHeap::new();

        // Add all connections to the min-heap
        for connection in connections {
            let (x, y, cost) = (connection[0] as usize - 1, connection[1] as usize - 1, connection[2]);
            edges.push(Reverse((cost, x, y)));
        }

        let mut uf = UnionFind::new(n);
        let mut total_cost = 0;

        // Kruskal's algorithm
        while let Some(Reverse((cost, x, y))) = edges.pop() {
            if uf.union(x, y) {
                total_cost += cost;
                if uf.components == 1 {
                    return total_cost;
                }
            }
        }

        -1 // Unable to connect all cities
    }
}