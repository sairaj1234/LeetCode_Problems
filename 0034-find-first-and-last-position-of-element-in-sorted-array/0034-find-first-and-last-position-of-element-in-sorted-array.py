class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        k=0
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
                break
        for j in range(len(nums)):
            
            if nums[len(nums)-1-j]==target:
                l.append(len(nums)-1-j)
                
                break
       
        if len(l)==0:
            return [-1,-1]
        return l
        