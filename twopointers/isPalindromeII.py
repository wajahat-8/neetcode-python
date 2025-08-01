class Solution:
    def validPalindromeII(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# Testing
sol = Solution()
print(sol.validPalindromeII("abca"))     # True
print(sol.validPalindromeII("racecar"))  # True
print(sol.validPalindromeII("abc"))      # False
