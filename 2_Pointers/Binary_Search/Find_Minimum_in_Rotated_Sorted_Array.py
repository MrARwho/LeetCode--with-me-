class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        left,right = 0 , len(nums)-1
        min1 = nums[left]
        
        while (left <= right):
            mid = (left+right)//2
            min1 = min(min1, nums[mid])
            print("left : " , left , "right : " , right)
            
            
            
            if(nums[left] <= nums[mid]):
                left = mid+1
                
            else:
                right = mid-1
                
        return min1
            

a = Solution()
b = [3,4,5,1,2]
print(a.findMin(b))
                
            