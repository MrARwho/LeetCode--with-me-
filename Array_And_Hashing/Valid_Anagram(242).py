class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s.sort()
        t.sort()
        if sorted(s) ==sorted(t) :
            return True
        else:
            return False
        

x = 'axpza'
print(sorted(x))