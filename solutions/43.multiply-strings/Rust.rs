impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            return "0".to_string();
        }

        let num1_bytes = num1.as_bytes();
        let num2_bytes = num2.as_bytes();
        let mut result = vec![0; num1.len() + num2.len()];

        for i in (0..num1.len()).rev() {
            for j in (0..num2.len()).rev() {
                let mul = (num1_bytes[i] - b'0') as usize * (num2_bytes[j] - b'0') as usize;
                let p1 = i + j;
                let p2 = i + j + 1;
                let sum = mul + result[p2];

                result[p2] = sum % 10;
                result[p1] += sum / 10;
            }
        }

        let mut result_str = String::new();
        let mut leading_zero = true;

        for &num in &result {
            if num != 0 {
                leading_zero = false;
            }
            if !leading_zero {
                result_str.push((num as u8 + b'0') as char);
            }
        }

        result_str
    }
}
