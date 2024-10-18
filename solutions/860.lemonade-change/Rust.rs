impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        let mut five_count = 0;
        let mut ten_count = 0;
        
        for bill in bills {
            match bill {
                5 => {
                    five_count += 1;
                },
                10 => {
                    if five_count > 0 {
                        five_count -= 1;
                        ten_count += 1;
                    } else {
                        return false;
                    }
                },
                20 => {
                    if ten_count > 0 && five_count > 0 {
                        ten_count -= 1;
                        five_count -= 1;
                    } else if five_count >= 3 {
                        five_count -= 3;
                    } else {
                        return false;
                    }
                },
                _ => {
                    // This case should not happen as per the problem constraints
                    return false;
                }
            }
        }
        
        true
    }
}
