
from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        valid = False
        
        
        
        for i in range(len(s)):
            print(s[i])
            if (s[i] == '{' or s[i] == '(' or s[i] == '['):
                stack.append(s[i])
                valid = False
            elif((s[i] == '}' or s[i] == ')' or s[i] == ']' ) and (len(stack) > 0)):
                a = stack.pop()
                if(s[i] == '}' and a == '{'):
                    valid = True
                elif(s[i] == ']' and a == '['):
                    valid =  True
                elif(s[i] == ')' and a == '('):
                    valid = True
                else:
                    return False
            else:
                return False
        
        if (len(stack)):
            return False          
                    
        else :
            return valid
    
a = Solution()
s = "([]"

    
print(a.isValid(s))
                
                
        
        
        