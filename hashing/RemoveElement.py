class Solution:
    def removeElement(self,nums,val):
        count=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
        return count
nums=[3,2,2,3,1]
val=3
solution=Solution()
new_length=solution.removeElement(nums,val)
print(f"New length: {new_length}")
print(f"Modified array: {nums[:new_length]}")