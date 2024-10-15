class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def is_match(pattern_idx, s_idx, pattern_to_string, string_to_pattern):
            if pattern_idx == len(pattern) and s_idx == len(s):
                return True
            if pattern_idx == len(pattern) or s_idx == len(s):
                return False

            current_char = pattern[pattern_idx]

            for end in range(s_idx + 1, len(s) + 1):
                candidate = s[s_idx:end]

                if current_char not in pattern_to_string and candidate not in string_to_pattern:
                    pattern_to_string[current_char] = candidate
                    string_to_pattern[candidate] = current_char

                    if is_match(pattern_idx + 1, end, pattern_to_string, string_to_pattern):
                        return True

                    del pattern_to_string[current_char]
                    del string_to_pattern[candidate]
                elif current_char in pattern_to_string and pattern_to_string[current_char] == candidate:
                    if is_match(pattern_idx + 1, end, pattern_to_string, string_to_pattern):
                        return True

            return False

        return is_match(0, 0, {}, {})