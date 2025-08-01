from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while (
                1 <= nums[i] <= n and
                nums[nums[i] - 1] != nums[i]
            ):
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
sol = Solution()
print(sol.firstMissingPositive([3, 4, -1, 1]))  # Output: 2
print(sol.firstMissingPositive([1, 2, 0]))      # Output: 3
print(sol.firstMissingPositive([7, 8, 9, 11]))  # Output: 1
