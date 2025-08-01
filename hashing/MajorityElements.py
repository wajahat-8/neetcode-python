class Solution:
    def majorityElement(self,nums):
        count=0
        current=0
        for num in nums:
            if count==0 or num==current:
                current=num
                count+=1
            else:
                count-=1
        return current
nums = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
result = solution.majorityElement(nums)

print(f"Majority element is: {result}")