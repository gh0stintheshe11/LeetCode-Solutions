impl Solution {
    pub fn largest_number(nums: Vec<i32>) -> String {
        // Convert the numbers to strings
        let mut num_strs: Vec<String> = nums.iter().map(|&num| num.to_string()).collect();
        
        // Sort the strings using a custom comparator
        num_strs.sort_by(|a, b| {
            let order1 = format!("{}{}", a, b);
            let order2 = format!("{}{}", b, a);
            order2.cmp(&order1)
        });
        
        // Join the sorted strings
        let result = num_strs.join("");
        
        // Handle the case where the result is all zeros
        if result.chars().next().unwrap() == '0' {
            "0".to_string()
        } else {
            result
        }
    }
}
