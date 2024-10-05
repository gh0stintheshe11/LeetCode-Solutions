use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn can_cross(stones: Vec<i32>) -> bool {
        let stone_set: HashSet<i32> = stones.iter().cloned().collect();
        let mut memo: HashMap<(usize, i32), bool> = HashMap::new();
        Self::can_cross_from(&stones, 0, 0, &stone_set, &mut memo)
    }

    fn can_cross_from(
        stones: &Vec<i32>,
        pos: usize,
        last_jump: i32,
        stone_set: &HashSet<i32>,
        memo: &mut HashMap<(usize, i32), bool>,
    ) -> bool {
        if pos == stones.len() - 1 {
            return true;
        }

        if let Some(&result) = memo.get(&(pos, last_jump)) {
            return result;
        }

        let current_stone = stones[pos];
        for jump in [last_jump - 1, last_jump, last_jump + 1].iter().cloned() {
            if jump > 0 {
                let next_stone = current_stone + jump;
                if stone_set.contains(&next_stone) {
                    if let Some(next_pos) = stones.iter().position(|&x| x == next_stone) {
                        if Self::can_cross_from(stones, next_pos, jump, stone_set, memo) {
                            memo.insert((pos, last_jump), true);
                            return true;
                        }
                    }
                }
            }
        }

        memo.insert((pos, last_jump), false);
        false
    }
}
