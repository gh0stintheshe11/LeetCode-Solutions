impl Solution {
    pub fn maximum_score(nums: Vec<i32>, multipliers: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = multipliers.len();
        let mut memo = vec![vec![None; m + 1]; m + 1];
        
        fn dp(i: usize, left: usize, nums: &Vec<i32>, multipliers: &Vec<i32>, memo: &mut Vec<Vec<Option<i32>>>) -> i32 {
            if i == multipliers.len() {
                return 0;
            }
            if let Some(result) = memo[i][left] {
                return result;
            }
            let right = nums.len() - 1 - (i - left);
            let choose_left = multipliers[i] * nums[left] + dp(i + 1, left + 1, nums, multipliers, memo);
            let choose_right = multipliers[i] * nums[right] + dp(i + 1, left, nums, multipliers, memo);
            let result = choose_left.max(choose_right);
            memo[i][left] = Some(result);
            result
        }
        
        dp(0, 0, &nums, &multipliers, &mut memo)
    }
}
