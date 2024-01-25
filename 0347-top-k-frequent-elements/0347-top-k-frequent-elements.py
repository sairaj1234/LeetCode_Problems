from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count_numbers=Counter(nums)
        m=[key for key,  Count in Count_numbers.most_common(k)]
        return m
                
        