class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []
        self.increments = [0] * maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1
        index = len(self.stack) - 1
        if index > 0:
            self.increments[index - 1] += self.increments[index]
        value = self.stack.pop() + self.increments[index]
        self.increments[index] = 0
        return value

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if k > 0 and self.stack:
            k = min(k, len(self.stack))
            self.increments[k - 1] += val
