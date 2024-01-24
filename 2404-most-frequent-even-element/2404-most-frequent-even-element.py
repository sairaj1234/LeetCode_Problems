class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        l=[]
        n=0
        k,k1=-1,0
        for i in nums:
            if i%2==0:
                if i not in l:
                    l.append(i)
                    n1=nums.count(i)
                    
                    if n==n1:
                        k1=i
                        if k>k1:
                            k=k1
                    elif n<n1:
                        n=n1
                        k=i
                        
        return k
                    
                            
                        
                    
        