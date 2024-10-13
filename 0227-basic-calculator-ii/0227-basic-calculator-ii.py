class Solution(object):
    def calculate(self, s):
        val = 0
        si = "+"
        n = len(s)
        current_result = 0
        last_val = 0

        for i, char in enumerate(s):
            if char.isdigit():
                val = val * 10 + int(char)

            if i == n - 1 or char in "+-*/":
                if si == "+":
                    current_result += last_val
                    last_val = val
                elif si == "-":
                    current_result += last_val
                    last_val = -val
                elif si == "*":
                    last_val *= val
                elif si == "/":
                    if last_val // val < 0 and last_val % val != 0:
                        last_val = last_val // val + 1
                    else:
                        last_val //= val
                si = char
                val = 0

        current_result += last_val
        return current_result
