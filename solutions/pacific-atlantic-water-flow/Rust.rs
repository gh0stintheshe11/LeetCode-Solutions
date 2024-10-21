impl Solution {
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if heights.is_empty() || heights[0].is_empty() {
            return vec![];
        }

        let m = heights.len();
        let n = heights[0].len();
        let mut pacific = vec![vec![false; n]; m];
        let mut atlantic = vec![vec![false; n]; m];

        // DFS from top and bottom borders
        for i in 0..n {
            Self::dfs(&heights, 0, i as i32, &mut pacific, -1);
            Self::dfs(&heights, (m - 1) as i32, i as i32, &mut atlantic, -1);
        }

        // DFS from left and right borders
        for i in 0..m {
            Self::dfs(&heights, i as i32, 0, &mut pacific, -1);
            Self::dfs(&heights, i as i32, (n - 1) as i32, &mut atlantic, -1);
        }

        // Find cells reachable from both oceans
        let mut result = vec![];
        for i in 0..m {
            for j in 0..n {
                if pacific[i][j] && atlantic[i][j] {
                    result.push(vec![i as i32, j as i32]);
                }
            }
        }

        result
    }

    fn dfs(heights: &Vec<Vec<i32>>, i: i32, j: i32, visited: &mut Vec<Vec<bool>>, prev_height: i32) {
        if i < 0 || i >= heights.len() as i32 || j < 0 || j >= heights[0].len() as i32 
            || visited[i as usize][j as usize] || heights[i as usize][j as usize] < prev_height {
            return;
        }

        visited[i as usize][j as usize] = true;

        let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        for (di, dj) in directions.iter() {
            Self::dfs(heights, i + di, j + dj, visited, heights[i as usize][j as usize]);
        }
    }
}