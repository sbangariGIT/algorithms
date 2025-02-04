class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] < val:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(val)
            self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return -1
        return self.min_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()