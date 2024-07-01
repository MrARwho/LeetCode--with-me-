class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False
        start = 0
        second = start+2
        
        while second <= len(arr)-1:
            if arr[second]%2==1 and arr[start]%2==1 and arr[start+1]%2==1:
                return True
            else:
                start+=1
                second+=1
        return False

a = Solution()
arr = [2,6,4,1]
print(a.threeConsecutiveOdds(arr))