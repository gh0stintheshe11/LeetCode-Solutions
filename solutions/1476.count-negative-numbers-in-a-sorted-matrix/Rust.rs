impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut count = 0;
        let mut row = grid.len() as i32 - 1;
        let mut col = 0;
        let n = grid[0].len() as i32;

        while row >= 0 && col < n {
            if grid[row as usize][col as usize] < 0 {
                // All elements to the right of this element are also negative
                count += n - col;
                row -= 1;
            } else {
                col += 1;
            }
        }

        count
    }
}
