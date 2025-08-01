from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k > n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


solution = Solution()

    # Example input
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print("Original array:", nums)
solution.rotate(nums, k)
print("Rotated array by", k, "steps:", nums)
