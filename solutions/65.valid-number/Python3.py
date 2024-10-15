class Solution:
    def isNumber(self, s: str) -> bool:
        # Define states
        STATE_INITIAL = 0
        STATE_SIGN = 1
        STATE_INTEGER = 2
        STATE_POINT = 3
        STATE_POINT_WITHOUT_INT = 4
        STATE_FRACTION = 5
        STATE_EXP = 6
        STATE_EXP_SIGN = 7
        STATE_EXP_NUMBER = 8
        STATE_END = 9
        
        # Define the state transition table
        state = STATE_INITIAL
        for char in s:
            if state == STATE_INITIAL:
                if char in '+-':
                    state = STATE_SIGN
                elif char.isdigit():
                    state = STATE_INTEGER
                elif char == '.':
                    state = STATE_POINT_WITHOUT_INT
                else:
                    return False
            elif state == STATE_SIGN:
                if char.isdigit():
                    state = STATE_INTEGER
                elif char == '.':
                    state = STATE_POINT_WITHOUT_INT
                else:
                    return False
            elif state == STATE_INTEGER:
                if char.isdigit():
                    state = STATE_INTEGER
                elif char == '.':
                    state = STATE_POINT
                elif char in 'eE':
                    state = STATE_EXP
                else:
                    return False
            elif state == STATE_POINT:
                if char.isdigit():
                    state = STATE_FRACTION
                elif char in 'eE':
                    state = STATE_EXP
                else:
                    return False
            elif state == STATE_POINT_WITHOUT_INT:
                if char.isdigit():
                    state = STATE_FRACTION
                else:
                    return False
            elif state == STATE_FRACTION:
                if char.isdigit():
                    state = STATE_FRACTION
                elif char in 'eE':
                    state = STATE_EXP
                else:
                    return False
            elif state == STATE_EXP:
                if char in '+-':
                    state = STATE_EXP_SIGN
                elif char.isdigit():
                    state = STATE_EXP_NUMBER
                else:
                    return False
            elif state == STATE_EXP_SIGN:
                if char.isdigit():
                    state = STATE_EXP_NUMBER
                else:
                    return False
            elif state == STATE_EXP_NUMBER:
                if char.isdigit():
                    state = STATE_EXP_NUMBER
                else:
                    return False
            else:
                return False
        
        # Valid end states are those where the string can end
        return state in [STATE_INTEGER, STATE_POINT, STATE_FRACTION, STATE_EXP_NUMBER]
