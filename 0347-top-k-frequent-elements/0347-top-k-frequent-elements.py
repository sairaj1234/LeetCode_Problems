from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count_numbers=Counter(nums)#counter which count the number of each char store #in the form dict
        l=[]
        for key,value in Count_numbers.most_common(k):#mostcommon is used for sort the values and if given any value in it like here we given k so the number of values will return 
            l.append(key)
        return l
                
         