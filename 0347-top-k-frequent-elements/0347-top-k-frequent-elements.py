from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count_numbers=Counter(nums)
        l=[]
        for key,value in Count_numbers.most_common(k):
            l.append(key)
        return l
                
        