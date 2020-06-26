class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.min_value) == 0 or x <= self.min_value[-1]:
            self.min_value.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.min_value[-1]:
            self.min_value = self.min_value[:-1]
        self.stack = self.stack[:-1]

    def top(self):
        """
        :rtype: int
        """
        if self.stack == []:
            return self.stack
        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        if self.min_value == []:
            return self.min_value
        return self.min_value[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()