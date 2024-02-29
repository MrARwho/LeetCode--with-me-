class MinStack(object):

    def __init__(self):
        self.stack  = []
        self.min = 2**31
        self.minarr = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if (not len(self.stack)):
            self.minarr.append(val)
            self.min = val
            self.stack.append(val)
        elif (val <= self.min):
            self.minarr.append(self.min)
            self.stack.append(val)
            self.min = val
        else:
            self.minarr.append(self.min)
            self.stack.append(val)

            
        

    def pop(self):
        """
        :rtype: None
        """
        if(len(self.stack) == 0):
            print("Error stack is empty")
        elif(self.stack[-1] == self.min):
            self.min = self.minarr[-1]
            del self.stack[-1]
            del self.minarr[-1]
        else:
            del self.stack[-1]
            del self.minarr[-1]
            
    
        
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1]
    
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.min
        
        


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
minStack.top()
print(minStack.getMin())