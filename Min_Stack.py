class MinStack:

## With O(1) time complexity and two stacks ##
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x<=self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # print(self.stack)
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:
## With push and pop being O(n) time complexity ##
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        print("Before: ",self.stack)
        if len(self.stack) == 0:
            self.stack.append(x)
        else:
            for i in range(len(self.stack)):
                if i == len(self.stack)-1:
                    self.stack.append(x)
        print("After: ", self.stack)

    def pop(self) -> None:
        for i in range(len(self.stack)):
            if i == len(self.stack)-1:
                self.stack.pop(i)
        print(self.stack)

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        # print(self.stack)
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
