class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        max = 0
        i = 0
        j = len(height)-1
        while i != j :
            print(i , j)
            if (height[i] >= height[j]):
                vol = height[j]*(j-i)
                if (vol > max):
                    max = vol
                j-=1
            elif(height[j] >= height[i]):
                vol = height[i]*(j-i)
                if (vol > max):
                    max = vol
                i +=1
        return max
    
a= Solution()
f =[1,1]
print(a.maxArea(f))