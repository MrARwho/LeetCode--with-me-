class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        print(nums)
        
        count={}
        lst =[]
        count1=0
        for i in range(len(nums)):
            if (i < len(nums)-1):
                if (nums[i] == nums[i+1] ):
                    count1 +=1
                    print(nums[i])
                else:
                    count.update({nums[i]:count1+1})
                    count1 = 0
            else:
                    count.update({nums[i]:count1+1})
                    count1 = 0
        for i in range(k) :
            lst.append((max(count,key = count.get)))
            del count[max(count ,key = count.get)]
        return lst
    
    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {}
        freq = [[] for i in range(len(nums) + 1)] #generates list of n(length of input array) empty lists 

        for n in nums: 
            count[n] = 1 + count.get(n, 0) #if n is present in the hash then increment by 1 else default 0 
        for n,c in count.items():
            # n appears c no of times 
            freq[c].append(n) #append the value 'n' at the index 'c'th array 
        
        res = []
        # reverse traverse the freq array and append the top elements to result
        for i in range(len(freq) - 1, -1, -1): 
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

a  = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(a.topKFrequent(nums , k))