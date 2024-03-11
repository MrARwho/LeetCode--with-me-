class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        arr = []
        for i in range(len(nums)):
            if (i>0 and ( nums[i] == nums[i-1])): continue
            st = i+1
            en = len(nums) - 1
            while(st < en):
                ans = nums[i]
                ans +=  + nums[en] + nums[st]
                if ans == 0:
                    arr.append([nums[i],nums[st],nums[en]])
                    st+=1
                    en-=1
                    while(st<en and (nums[st] == nums[st-1])):
                        st+=1
                    while(st<en and (nums[en] == nums[en+1])):
                        en-=1
                elif ans < 0:
                    st+=1
                else:
                    en-=1
        return arr