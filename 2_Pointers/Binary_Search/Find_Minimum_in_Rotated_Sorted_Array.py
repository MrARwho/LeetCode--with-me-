class Solution:
    def findMin(self, nums: list[int]) -> int:
         left,right = 0 , len(nums)-1
         
         while (left != right):
            mid = (left+right)>>2
            print("left : " , left , "right : " , right)
            if (nums[mid+1] > nums[mid] and nums[mid-1] > nums[mid]):
                print("h")
                return nums[mid]
            elif(nums[left]>nums[mid]):
                left = mid+1
                
            elif(nums[mid]<nums[right]):
                right = mid
            

a = Solution()
b = [3,4,5,1,2]
print(a.findMin(b))
                
            