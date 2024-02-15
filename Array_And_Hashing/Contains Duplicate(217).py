class Solution(object):
    # This approch uses Hashset complexity = O(n)
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        ret = False
        for i in range(len(nums)):
            if nums[i] in dic:
                ret = True
                break
            else:
                print("inn")
                dic.update({nums[i]:i})
        return ret
    
    
    # This approch uses Sorted arry complexity = O(n)
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ret = False
        nums.sort()
        for i in range(1,len(nums)):
            if (nums[i] == nums[i-1]):
                return True
        return False      

a = Solution()
arr = [3,3]

print(a.containsDuplicate(arr))
print(a.containsDuplicate2(arr))