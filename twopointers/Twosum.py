class Solution:
    def twoSum(self,numbers,target):
        left=0
        right=len(numbers)-1

        while left<=right:
            sum_=numbers[left]+numbers[right]
            if sum_==target:
                return [left+1,right+1]
            elif sum_<target:
                left+=1
            else:
                right-=1

        return [-1,-1]
sol=Solution()
print(sol.twoSum([2,7,11,15],9))