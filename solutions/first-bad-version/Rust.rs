// The API isBadVersion is defined for you.
// isBadVersion(version:i32)-> bool;
// to call it use self.isBadVersion(version)

impl Solution {
    pub fn first_bad_version(&self, n: i32) -> i32 {
        let mut left = 1;
        let mut right = n;
        
        while left < right {
            let mid = left + (right - left) / 2;
            if self.isBadVersion(mid) {
                right = mid; // The first bad version is in the left half (including mid)
            } else {
                left = mid + 1; // The first bad version is in the right half (excluding mid)
            }
        }
        
        left // or right, since left == right at this point
    }
}
