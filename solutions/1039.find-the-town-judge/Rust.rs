impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut trust_count = vec![0; n + 1];  // +1 because people are labeled from 1 to n

        for pair in trust {
            trust_count[pair[0] as usize] -= 1;  // person who trusts
            trust_count[pair[1] as usize] += 1;  // person who is trusted
        }

        for i in 1..=n {
            if trust_count[i] == n as i32 - 1 {
                return i as i32;
            }
        }

        -1  // no town judge found
    }
}