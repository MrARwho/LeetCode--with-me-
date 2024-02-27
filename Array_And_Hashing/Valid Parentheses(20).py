
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
            if (s[i] == '{' or s[i] == '(' or s[i] == '['  or i == 0):
                print("pushed : " , s[i])
                stack.append(s[i])
            elif((s[i] == '}' or s[i] == ')' or s[i] == ']' ) and (len(stack) > 0)):
                a = stack.pop()
                if(s[i] == '}' and a == '{'):
                    valid = True
                    print("stack poped : " , a , ' i : ' , s[i])
                elif(s[i] == ']' and a == '['):
                    print("stack poped : " , a , ' i : ' , s[i])
                    valid =  True
                elif(s[i] == ')' and a == '('):
                    print("stack poped : " , a , ' i : ' , s[i])
                    valid = True
                else:
                    print("stack poped : " , a , ' i : ' , s[i])
                    valid = False
                    return False
                    
                    
        return valid
    
a = Solution()
s = "(){}}{"

for i in s:
    print (i)
    
print(a.isValid(s))
                
                
        
        
        