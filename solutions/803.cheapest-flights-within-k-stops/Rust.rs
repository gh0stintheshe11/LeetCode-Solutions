use std::collections::HashMap;

impl Solution {
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
        let mut prices = vec![i32::MAX; n as usize];
        prices[src as usize] = 0;
        
        let mut graph: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();
        for flight in flights {
            graph.entry(flight[0]).or_insert(Vec::new()).push((flight[1], flight[2]));
        }
        
        let mut temp_prices = prices.clone();
        
        for _ in 0..=k {
            for from in 0..n {
                if prices[from as usize] == i32::MAX {
                    continue;
                }
                
                if let Some(neighbors) = graph.get(&from) {
                    for &(to, price) in neighbors {
                        if prices[from as usize] + price < temp_prices[to as usize] {
                            temp_prices[to as usize] = prices[from as usize] + price;
                        }
                    }
                }
            }
            prices = temp_prices.clone();
        }
        
        if prices[dst as usize] == i32::MAX {
            -1
        } else {
            prices[dst as usize]
        }
    }
}