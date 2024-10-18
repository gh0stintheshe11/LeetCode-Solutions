impl Solution {
    pub fn successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        let mut potions = potions;
        potions.sort();
        let m = potions.len();
        let mut result = Vec::with_capacity(spells.len());

        for &spell in &spells {
            let mut left = 0;
            let mut right = m;
            while left < right {
                let mid = left + (right - left) / 2;
                if (spell as i64) * (potions[mid] as i64) >= success {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            result.push((m - left) as i32);
        }

        result
    }
}
