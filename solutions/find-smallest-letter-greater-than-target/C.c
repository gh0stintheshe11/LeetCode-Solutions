char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int left = 0;
    int right = lettersSize - 1;

    // If the target is greater than or equal to the last element, return the first element
    if (target >= letters[right]) {
        return letters[0];
    }

    // Binary search to find the smallest character greater than target
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (letters[mid] > target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return letters[left];
}
