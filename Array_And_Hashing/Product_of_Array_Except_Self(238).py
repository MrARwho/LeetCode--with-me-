class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        post = [1 for i in range(len(nums))]
        pre = [1 for i in range(len(nums))]
        ans = [1 for i in range(len(nums))]

        
        post [0] = 1        
        pre [len(nums)-1] = 1
        
        for i in range(1,len(nums)):
            post[i] = post[i-1] * nums[i-1]
        print(post)
        for i in range(len(nums)-2,0-1,-1):
            pre[i] = pre[i+1] * nums [i+1]
        print(pre)
        for i in range(len(nums)):
            ans[i] = post[i] * pre[i]
        
        return ans
            
        
        
a = Solution()
b = [1,2,3,4]
print(a.productExceptSelf(b))