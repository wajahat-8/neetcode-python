from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the position of '#' which separates length and string
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # extract length
            i = j + 1             # skip past '#'
            j = i + length        # get the end of the string
            res.append(s[i:j])    # extract the string
            i = j                 # move to the next segment
        return res

# ✅ Test the code
sol = Solution()
original = ["leet", "code", "rocks", "123", "emoji"]
encoded = sol.encode(original)
decoded = sol.decode(encoded)

print("Original:", original)
print("Encoded :", encoded)
print("Decoded :", decoded)
print("Match?  :", original == decoded)
