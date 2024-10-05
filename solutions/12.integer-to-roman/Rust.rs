impl Solution {
    /// Converts an integer to a Roman numeral.
    ///
    /// # Arguments
    ///
    /// * `num` - An integer between 1 and 3999 inclusive.
    ///
    /// # Returns
    ///
    /// * A `String` representing the Roman numeral equivalent of the input integer.
    pub fn int_to_roman(mut num: i32) -> String {
        // List of value-symbol pairs sorted in descending order, including subtractive pairs
        let val_sym = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ];

        let mut result = String::new();

        for &(value, symbol) in val_sym.iter() {
            while num >= value {
                result.push_str(symbol);
                num -= value;
            }
            if num == 0 {
                break;
            }
        }

        result
    }
}