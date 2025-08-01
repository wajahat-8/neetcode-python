class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        chars = list(cleaned)
        left = 0
        right = len(chars) - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        result = ''.join(chars)
        return cleaned == result

# Example usage
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))                      # False
