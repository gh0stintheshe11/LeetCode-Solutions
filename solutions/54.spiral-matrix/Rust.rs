impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        if matrix.is_empty() {
            return vec![];
        }

        let mut result = Vec::new();
        let (mut top, mut bottom) = (0, matrix.len() as i32 - 1);
        let (mut left, mut right) = (0, matrix[0].len() as i32 - 1);

        while top <= bottom && left <= right {
            // Traverse from left to right along the top row
            for j in left..=right {
                result.push(matrix[top as usize][j as usize]);
            }
            top += 1;

            // Traverse from top to bottom along the right column
            for i in top..=bottom {
                result.push(matrix[i as usize][right as usize]);
            }
            right -= 1;

            if top <= bottom {
                // Traverse from right to left along the bottom row
                for j in (left..=right).rev() {
                    result.push(matrix[bottom as usize][j as usize]);
                }
                bottom -= 1;
            }

            if left <= right {
                // Traverse from bottom to top along the left column
                for i in (top..=bottom).rev() {
                    result.push(matrix[i as usize][left as usize]);
                }
                left += 1;
            }
        }

        result
    }
}
