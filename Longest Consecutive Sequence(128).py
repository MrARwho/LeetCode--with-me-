class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums == []):
            return 0
        nums.sort()
        print(nums)
        count = 1
        countarr = []
        for i in range(0,len(nums)):
            if (nums[i]-1 == nums[i-1] ):
                count+=1
                print(count)
                if (i == len(nums)-1):
                    countarr.append(count)
            elif(nums[i] == nums[i-1]):
                countarr.append(count)
                continue
            else: 
                countarr.append(count)
                print("else ",count)
                count = 1
            
        
        print(countarr)
        countarr.sort(reverse=True)
        return countarr[0]
    
a = Solution()
nums = [0,0]
print(a.longestConsecutive(nums))
        
        
