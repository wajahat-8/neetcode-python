from typing import List
class Solution:
    def sortColors(self,nums: List[int])->None:
        left=0
        mid=0
        right=len(nums)-1

        while mid <= right:
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                left+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
nums = [2, 0, 2, 1, 1, 0]
print("Before sorting:", nums)

solution = Solution()
solution.sortColors(nums)

print("After sorting: ", nums)