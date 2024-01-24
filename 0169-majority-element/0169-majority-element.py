class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=[]
        n=0
        k=0
        for i in nums:
            if i not in l:
                l.append(i)
                n1=nums.count(i)
                if n<n1:
                    n=n1
                    k=i

        return k
