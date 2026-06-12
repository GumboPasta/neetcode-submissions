from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Key Data Structure: Stack

        # Stores operands and intermediate results
        stk = []

        # Process each token from left to right
        for t in tokens:

            # If the token is an operator, perform the operation
            if t in '+-*/':

                # Pop the two most recent operands
                # IMPORTANT: order matters for subtraction and division
                b, a = stk.pop(), stk.pop()

                # Perform the corresponding operation and
                # push the result back onto the stack
                if t == '+':
                    stk.append(a + b)
                elif t == '-':
                    stk.append(a - b)
                elif t == '*':
                    stk.append(a * b)
                else:
                    # LeetCode requires division to truncate toward zero
                    division = a / b

                    # Negative values need ceil() to truncate toward zero
                    if division < 0:
                        stk.append(ceil(division))
                    # Positive values need floor() to truncate toward zero
                    else:
                        stk.append(floor(division))

            # Otherwise, the token is a number
            # Convert it to an integer and push it onto the stack
            else:
                stk.append(int(t))

        # After processing all tokens, the final answer
        # will be the only value remaining in the stack
        return stk[0]

        # Time Complexity: O(n)
        # Space Complexity: O(n)