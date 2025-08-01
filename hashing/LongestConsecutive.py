class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        number_set = set(nums)
        longest_streak = 0

        for num in number_set:
            if num - 1 not in number_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in number_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Test
sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
