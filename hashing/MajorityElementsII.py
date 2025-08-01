from typing import List
class Solution:
    def majorityElement(self,nums: List[int])->List[int]:
        num1,num2,count1,count2=-1,-1,0,0
        for num in nums:
            if num==num1:
                count1+=1
            elif num==num2:
                count2+=1
            elif count1==0:
                num1,count1=num,1
            elif count2==0:
                num2,count2=num,1
            else:
                count1-=1
                count2-=1
        count1=count2=0
        for num in nums:
            if num==num1:
                count1+=1
            elif num==num2:
                count2+=1
        result=[]
        n=len(nums)//3
        if count1>n:
            result.append(num1)
        if count2>n:
            result.append(num2)
        return result

sol = Solution()
print(sol.majorityElement([3,2,3]))         # Output: [3]
print(sol.majorityElement([1,1,1,3,3,2,2,2])) # Output: [1,2]
