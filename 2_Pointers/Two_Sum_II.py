class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        j = len(numbers)-1
        i = 0
        while i<j:
            if ((numbers[i] + numbers[j])> target):
                j-=1
            elif(((numbers[i] + numbers[j])< target)):
                i+=1
            else:
                return [i+1 , j+1]

numbers = [2,3,4]
a = Solution()
print(a.twoSum(numbers,6))