from typing import List

class Solution:
    def sortArray(self,nums:List[int])->List[int]:

        self.merge_sort(nums,0 ,len(nums)-1)
        return nums

    def merge_sort(self,array:List[int],left:int,right:int)->None:
        if left<right:
            mid=left+(right-left)//2
            self.merge_sort(array,left,mid)
            self.merge_sort(array,mid+1,right)
            self.merge(array,left,mid,right)
    def merge(self,array: List[int],left:int,mid:int,right:int)->None:
        sizeLeft=mid-left+1
        sizeRight=right-mid
        L=[0]*sizeLeft
        R=[0]*sizeRight

        for i in range(sizeLeft):
            L[i]=array[left+i]
        for j in range(sizeRight):
            R[j]=array[mid+1+j]
        i=j=0
        k=left
        while i<sizeLeft and j<sizeRight:
            if L[i]<=R[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=R[j]
                j+=1
            k+=1
        while i<sizeLeft:
            array[k]=L[i]
            i+=1
            k+=1
        while j<sizeRight:
            array[k]=R[j]
            j+=1
            k+=1
sol=Solution()
nums=[5, 2, 3, 1]
sorted_nums=sol.sortArray(nums)
print(sorted_nums)