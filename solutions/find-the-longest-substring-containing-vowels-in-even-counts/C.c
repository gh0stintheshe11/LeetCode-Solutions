#include <string.h>

int findTheLongestSubstring(char * s) {
    int n = strlen(s);

    // Mapping from characters 'a'-'z' to their corresponding vowel bits
    int vowel_to_bit[26];
    for (int i = 0; i < 26; i++) {
        vowel_to_bit[i] = -1;  // Initialize all characters as non-vowels
    }
    vowel_to_bit['a' - 'a'] = 0;  // Map 'a' to bit 0
    vowel_to_bit['e' - 'a'] = 1;  // Map 'e' to bit 1
    vowel_to_bit['i' - 'a'] = 2;  // Map 'i' to bit 2
    vowel_to_bit['o' - 'a'] = 3;  // Map 'o' to bit 3
    vowel_to_bit['u' - 'a'] = 4;  // Map 'u' to bit 4

    // Since there are 2^5 = 32 possible states for the vowels,
    // we use an array to store the earliest index at which each state occurs.
    int state_to_index[32];
    for (int i = 0; i < 32; i++) {
        state_to_index[i] = -2;  // Initialize all states as unseen
    }
    state_to_index[0] = -1;  // The initial state (all vowels even) occurs before the string starts

    int state = 0;      // Current state of vowel parity
    int max_length = 0; // Maximum length of substring found

    for (int i = 0; i < n; i++) {
        char c = s[i];
        int idx = c - 'a';  // Convert character to index (0-25)

        // Check if the character is a vowel
        if (vowel_to_bit[idx] != -1) {
            // Flip the corresponding bit in the state
            state ^= (1 << vowel_to_bit[idx]);
        }

        // If the state has been seen before, calculate the length of the substring
        if (state_to_index[state] != -2) {
            int length = i - state_to_index[state];
            if (length > max_length) {
                max_length = length;
            }
        } else {
            // Record the first occurrence of this state
            state_to_index[state] = i;
        }
    }

    return max_length;
}
