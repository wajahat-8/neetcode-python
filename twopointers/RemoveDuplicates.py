class Solution:
    def removeDuplicates(self,nums):
        if not nums:
            return 0

        count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[count-1]:
                nums[count]=nums[i]
                count+=1

        return count
sol=Solution()
nums = [1, 1, 2, 3, 3, 4]
k = sol.removeDuplicates(nums)

print("Unique count:", k)
print("Modified array (first k elements):", nums[:k])