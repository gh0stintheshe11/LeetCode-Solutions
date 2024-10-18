class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half_n = n // 2
        left_sum = right_sum = 0
        left_question_marks = right_question_marks = 0

        for i in range(half_n):
            if num[i] == '?':
                left_question_marks += 1
            else:
                left_sum += int(num[i])

        for i in range(half_n, n):
            if num[i] == '?':
                right_question_marks += 1
            else:
                right_sum += int(num[i])

        # Calculate the difference in sum and question marks
        balance_sum = left_sum - right_sum
        balance_question_marks = left_question_marks - right_question_marks

        # The difference between sums that needs to be compensated by '?' characters
        # balance_sum + 4.5 * balance_question_marks should be zero for Bob to win
        # As the '9' makes a difference of 9 and '0' makes a difference of 0
        if balance_sum * 2 == -balance_question_marks * 9:
            return False
        return True