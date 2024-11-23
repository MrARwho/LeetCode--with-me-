class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        i = 0
        if len(word1)> len(word2):
            while (i < len(word2)):
                output += word1[i] + word2[i]
                i+=1
            print('before : ' , output)
            output += word1[i:]
            print('after : ' , output)
        if len(word1)< len(word2):
            print("loop rin")
            while (i < len(word1)):
                output += word1[i] + word2[i]
                i+=1
            output += word2[i:]
        elif (len(word1) == len(word2)): 
            for i in range(len(word2)):
                output+= word1[i] + word2[i]
       
        return output
    


a = Solution()
print(a.mergeAlternately('abcd','pq'))