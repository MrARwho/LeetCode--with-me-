class Solution(object):
    # this uses 2 seperate arrays
    # 1 to store sorted words each anagram once
    
    # and then a for loop to compare and add them to second array
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a = []
        x = []
        for i in strs:
            if (sorted(i) not in a):
                if ([i] not in x and [i] not in a):
                    x.append([])
                a.append(sorted(i))
        for i in range(len(strs)):
            if (sorted(strs[i]) in a):
                x[a.index(sorted(strs[i]))].append(strs[i])
        return x
    
    # this uses a dictionary instead of 2 arrays 
    # checks if the anagram was stored previously and puts them as key value pair
    # sortedword: anagrams of that word
    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            print(sorted_word)
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        print(anagrams)
        return list(anagrams.values())
    
strs = ["eat","tea","tan","ate","nat","bat"]
y = Solution()
print(y.groupAnagrams2(strs))
            