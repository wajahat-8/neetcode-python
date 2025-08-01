from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self,nums:List[int],k:int)->int:
        sum_count=defaultdict(int)
        sum_count[0]=1

        prefix_sum=0
        count=0

        for num in nums:
            prefix_sum+=num

            if(prefix_sum-k) in sum_count:
                count+=sum_count[prefix_sum-k]

            sum_count[prefix_sum]+=1
        return count
sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))  # Output: 2
print(sol.subarraySum([1, 2, 3], 3))  # Output: 2
