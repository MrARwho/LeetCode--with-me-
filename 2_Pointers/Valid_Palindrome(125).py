class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # x = []
        # for i in s:
        #     if i in a:
        #         x.append(i)
                
        # j = -1
        # i=0
        # palin = True
        # print(x)
        # if (len(x) == 0):
        #     return True
        # for i in range(len(x)//2):
        #     if ((x[i]).lower() != x[j].lower()):
        #         print("X[I] : " ,x[i] , "X[j] : " ,x[j])
        #         return False
        #     else:
        #         j-=1
        # return palin
        
        x = []
        for i in s.lower():
            if i.isalnum():
                x.append(i)
        print(s)
        return x == x[::-1]
        
        
    

a = Solution()
s = "race a car"
print(a.isPalindrome(s))
    
