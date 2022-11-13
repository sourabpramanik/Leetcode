class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = list(s)
        self.reverse_arr(arr, 0, len(arr)-1)
        self.reverse_str(arr)
        word = self.trim_side(arr)
        ans = self.trim_dup_space(word)
        return "".join(ans)
    def reverse_arr(self, arr, l, r):
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
        return arr
    
    def reverse_str(self, arr):
        l=0
        r=0
        
        while r<len(arr):
            while r<len(arr) and not arr[r].isspace(): r+=1
            
            self.reverse_arr(arr, l, r-1)
            r+=1
            l=r            
        
        return arr
    
    def trim_side(self, arr):
        if "".join(arr).isspace():
            return []
        
        l=0
        r=len(arr)-1
        
        while l<r and arr[l].isspace():l+=1
        while l<r and arr[r].isspace():r-=1
            
        return arr[l:r+1]
    
    def trim_dup_space(self, word):
        if not word: 
            return []
        
        res = [word[0]]
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace():
                continue
            res.append(word[i])
        
        return res