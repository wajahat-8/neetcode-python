from collections import defaultdict
class Solution:
    def groupAnagrams(self,strs):
        map =defaultdict(list)
        for str_ in strs:
            char_array=sorted(str_)
            sorted_str="".join(char_array)
            map[sorted_str].append(str_)
        return list(map.values())
solution=Solution()
result=solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
