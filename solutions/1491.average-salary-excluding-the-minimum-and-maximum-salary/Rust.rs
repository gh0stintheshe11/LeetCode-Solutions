impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        // Find the minimum and maximum salary
        let min_salary = *salary.iter().min().unwrap();
        let max_salary = *salary.iter().max().unwrap();
        
        // Calculate the total sum of all salaries
        let total_sum: i32 = salary.iter().sum();
        
        // Calculate the sum excluding the minimum and maximum salary
        let sum_excluding_min_max = total_sum - min_salary - max_salary;
        
        // Calculate the number of elements excluding the minimum and maximum
        let count_excluding_min_max = (salary.len() - 2) as f64;
        
        // Calculate the average
        sum_excluding_min_max as f64 / count_excluding_min_max
    }
}
