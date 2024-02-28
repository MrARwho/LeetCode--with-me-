class MinStack(object):

    def __init__(self):
        self.stack  = []
        self.min = 2**31
        self.min2 = 0
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if (val < min):
            self.min = val
            self.min2 = self.min
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if(len(self.stack) == 0):
            print("Error stack is empty")
        else:
            self.stack.remove(len(self.stack)-1)
        
        

    def top(self):
        """
        :rtype: int
        """
        

    def getMin(self):
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()