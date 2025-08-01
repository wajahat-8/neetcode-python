class Solution:
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        min_length=min(len(s) for s in strs)
        prefix=[]
        for i in range(min_length):
            current_char=strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!= current_char:
                    return"".join(prefix)
            prefix.append(current_char)
        return "".join(prefix)
solution=Solution()
result=solution.longestCommonPrefix(["flower", "flow", "flight"])
print(result)