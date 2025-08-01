class Solution:
    def twoSum(self,nums,target):
        map={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in map:
                return [map[complement],i]
            map[nums[i]]=i
        return
solution=Solution()
result=solution.twoSum([2,7,11,15],9)
print(result)
