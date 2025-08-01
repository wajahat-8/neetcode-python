class solution:
    def containDuplicates(self,nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
sol=solution()
nums=[1,2,3,4,1]
result=sol.containDuplicates(nums)
print(f"Result is: {result}")