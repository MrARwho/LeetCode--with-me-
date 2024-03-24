class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right :
            mid = (left +right)//2
            if (nums[mid] == target):
                return mid 
            elif(nums[mid]>target):
                right = mid -1
                mid = ((right + left)//2)
            elif(nums[mid] < target):
                left = mid +1
                mid = (right + left)//2
            else:
                return -1
        return -1

a = Solution()
nums = [-1,0,3,5,9,12]
print(a.search(nums , 9))
                
                