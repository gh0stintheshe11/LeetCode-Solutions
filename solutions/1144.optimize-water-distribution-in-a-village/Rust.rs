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
    pub fn min_cost_to_supply_water(n: i32, wells: Vec<i32>, pipes: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut edges = BinaryHeap::new();

        // Add well costs as edges from virtual node 0 to each house
        for (i, &cost) in wells.iter().enumerate() {
            edges.push(Reverse((cost, 0, i + 1)));
        }

        // Add pipe costs
        for pipe in pipes {
            edges.push(Reverse((pipe[2], pipe[0] as usize, pipe[1] as usize)));
        }

        let mut uf = UnionFind::new(n + 1);  // +1 for the virtual node
        let mut total_cost = 0;
        let mut connected = 0;

        while let Some(Reverse((cost, house1, house2))) = edges.pop() {
            if uf.union(house1, house2) {
                total_cost += cost;
                connected += 1;
                if connected == n {
                    break;
                }
            }
        }

        total_cost
    }
}