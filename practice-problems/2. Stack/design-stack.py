# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.tmp = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.tmp) == 0 or x < self.tmp[-1]:
            self.tmp.append(x)
        else:
            self.tmp.append(self.tmp[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.tmp.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(self.tmp)
        return self.tmp[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
