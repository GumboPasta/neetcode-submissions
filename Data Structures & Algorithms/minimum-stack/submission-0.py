class MinStack:

    # Stack will operate as a normal stack
    # Min Stack will always store the minimum value at the top of the stack
    # Example:
    # [1,5,8,2]
    # Stack = [2,5,8,1]
    # MinStack = [2,2,2,1]


    def __init__(self):
        # Initialize Stack and Min Stack
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Stack just append
        self.stack.append(val)

        # For Min Stack, check if value is minimum
        if not self.minStack:
            self.minStack.append(val)
        elif self.minStack[-1] < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

    # Time Complexity: O(1)
    # Space Complexity: O(n)
        
