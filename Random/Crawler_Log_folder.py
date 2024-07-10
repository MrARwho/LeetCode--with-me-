
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        d =0 
        for i in logs:
            if(i == '../'):
                if(d == 0):
                    continue
                else:
                    d-=1
            elif(i == './'):
                continue
            else:
                d+=1
        
        if (d < 0):
            return 0 
        else:
            return d

a = Solution()
logs = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]
print(a.minOperations(logs))

        
