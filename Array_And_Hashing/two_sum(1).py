class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = {}
        sum = []
        for i in range(len(nums)):
            if ((target - nums[i]) in a):
                sum = [i,a.get(target - nums[i])]
                return sum
            else:
                a.update({nums[i]:i})
        
        return sum
    
x =[2,7,11,15]
b = Solution()
print(b.twoSum(x,9))
                