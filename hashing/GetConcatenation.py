class GetConcatenation:
    def getConcatination(self,nums):
        n=len(nums)
        ans=[0]*(n*2)
        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return ans
gc=GetConcatenation()
result=gc.getConcatination([1,2,3])
print(result)