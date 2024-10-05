use std::collections::HashSet;

impl Solution {
    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        let mut visited = HashSet::new();
        Self::dfs(&rooms, 0, &mut visited);
        visited.len() == rooms.len()
    }

    fn dfs(rooms: &Vec<Vec<i32>>, room: i32, visited: &mut HashSet<i32>) {
        if visited.contains(&room) {
            return;
        }

        visited.insert(room);

        for &key in &rooms[room as usize] {
            Self::dfs(rooms, key, visited);
        }
    }
}