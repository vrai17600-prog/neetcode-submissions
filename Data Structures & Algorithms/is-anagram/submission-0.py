from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        
        freq_map = dict(Counter(s))
        for c in t:
            freq_map[c] = freq_map.get(c,0) - 1
        return all(value==0 for value in freq_map.values())