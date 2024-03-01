from collections import deque
import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = deque()
        for i in tokens:
            if i == '*':
                a = stack.pop()
                b = stack.pop()
                c = a*b
                stack.append(int(c))
                
            elif i == '+':
                a = stack.pop()
                b = stack.pop()
                c = a+b
                stack.append(int(c))
            elif i == '/':
                
                a = stack.pop()
                b = stack.pop()
                
                c = int(b/a)
    
                stack.append((int(c)))
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                c = b-a
                stack.append(int(c))
            else:
                stack.append(int(i))
                
            
                
        return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
a = Solution()
print(a.evalRPN(tokens))

print(6/-132)
