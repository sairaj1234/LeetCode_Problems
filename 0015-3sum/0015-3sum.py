class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=set()
        
        j,k=1,len(nums)-1
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:

                if nums[i]+nums[j]+nums[k]==0:
                    
                    l.add((nums[i],nums[j],nums[k]))
                    j=j+1
                    k=k-1
                elif nums[i]+nums[j]+nums[k]<0:
                    j=j+1
                else:
                    k=k-1
        return list(l)
        