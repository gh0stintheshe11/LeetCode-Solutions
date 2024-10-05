use std::collections::{HashMap, HashSet};

struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl UnionFind {
    fn new(size: usize) -> Self {
        UnionFind {
            parent: (0..size).collect(),
            rank: vec![0; size],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]);
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let root_x = self.find(x);
        let root_y = self.find(y);
        if root_x != root_y {
            match self.rank[root_x].cmp(&self.rank[root_y]) {
                std::cmp::Ordering::Less => self.parent[root_x] = root_y,
                std::cmp::Ordering::Greater => self.parent[root_y] = root_x,
                std::cmp::Ordering::Equal => {
                    self.parent[root_y] = root_x;
                    self.rank[root_x] += 1;
                }
            }
        }
    }
}

impl Solution {
    pub fn accounts_merge(accounts: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let mut email_to_id: HashMap<String, usize> = HashMap::new();
        let mut email_to_name: HashMap<String, String> = HashMap::new();
        let mut id = 0;

        // Assign unique ID to each email and map email to name
        for account in &accounts {
            let name = &account[0];
            for email in account.iter().skip(1) {
                if !email_to_id.contains_key(email) {
                    email_to_id.insert(email.clone(), id);
                    id += 1;
                }
                email_to_name.insert(email.clone(), name.clone());
            }
        }

        // Union emails in the same account
        let mut uf = UnionFind::new(id);
        for account in &accounts {
            let first_email_id = *email_to_id.get(&account[1]).unwrap();
            for email in account.iter().skip(2) {
                uf.union(first_email_id, *email_to_id.get(email).unwrap());
            }
        }

        // Group emails by their root in the UnionFind
        let mut root_to_emails: HashMap<usize, HashSet<String>> = HashMap::new();
        for (email, &id) in &email_to_id {
            let root = uf.find(id);
            root_to_emails.entry(root).or_default().insert(email.clone());
        }

        // Build the final result
        let mut result = Vec::new();
        for emails in root_to_emails.values() {
            let mut account = Vec::new();
            let name = email_to_name.get(emails.iter().next().unwrap()).unwrap();
            account.push(name.clone());
            let mut sorted_emails: Vec<_> = emails.iter().cloned().collect();
            sorted_emails.sort();
            account.extend(sorted_emails);
            result.push(account);
        }

        result
    }
}