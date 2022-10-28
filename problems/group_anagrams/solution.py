class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for v in strs:
            l = list(v)
            l.sort()
            l = "".join(l)
            d[l].append(v)
        
        return d.values()