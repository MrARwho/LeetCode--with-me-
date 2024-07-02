class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        output = []
        if len(nums1)>=len(nums2):
            a=nums2
            b=nums1
        else:
            a=nums1
            b=nums2
        for i in a:
            if (i in b):
                b.remove(i)
                output.append(i)
                
        return output
    
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

a = Solution()
print(a.intersect(nums1,nums2))