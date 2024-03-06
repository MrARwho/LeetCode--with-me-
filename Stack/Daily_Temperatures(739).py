from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
       
        # stack = deque()
        # ans = [0]
        # for i, temperature in enumerate(temperatures):
        #     while stack and temperature > temperatures[stack[-1]]:
        #         index = stack.pop()
        #         ans[index] = i - index
        #     stack.append(i)
        # return ans
        ans = [0] * len(temperatures)
        stack = []  # a decreasing stack

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)

        return ans
        
temperatures = [73,74,75,71,69,72,76,73]
a =Solution()
print(a.dailyTemperatures(temperatures))