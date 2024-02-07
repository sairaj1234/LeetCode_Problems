class Solution:
    def frequencySort(self, s: str) -> str:
        Count_numbers=Counter(s)#counter which count the number of each char store #in the form dict{(3:4),(2:1),(4:5)}
        s=''
        for key,value in Count_numbers.most_common():#mostcommon is used for sort the values and if given any value in it like here we given k so the number of values will return ([(4:5),(3:4)])
            s=s+(key*value)
        
                
        return s
        
        