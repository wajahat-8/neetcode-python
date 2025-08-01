class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]

        suffix = 1
        for j in range(n - 1, -1, -1):
            ans[j] *= suffix
            suffix *= nums[j]

        return ans

sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
