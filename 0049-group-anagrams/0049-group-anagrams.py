class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        enum = {}
        for word in strs:
            a = "".join(sorted(word))
            
            if a in enum:
                enum[a].append(word)
            else:
                enum[a] = [word]
        
        return enum.values()
        
        