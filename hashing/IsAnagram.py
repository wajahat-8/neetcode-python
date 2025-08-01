class Solution:
    def isAnagram(self,s:str,t:str) -> bool:
        if len(s)!=len(t):
            return False
        freq=[0]*26
        for char in s:
            freq[ord(char)-ord('a')]+=1
        for char in t:
            if freq[ord(char)-ord('a')]==0:
                return False
            freq[ord(char)-ord('a')]-=1
            return True
solution=Solution()
result=solution.isAnagram("anagram","nagaram")
print(result)

result=solution.isAnagram("rat","car")
print(result)