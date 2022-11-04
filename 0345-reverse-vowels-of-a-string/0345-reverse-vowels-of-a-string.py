class Solution:
    def reverseVowels(self, s: str) -> str:
        vm = {"a","e","i","o","u"}
        
        i=0
        j=len(s)-1
        arr = list(s)
        
        while i<j:
            if arr[i].lower() in vm and arr[j].lower() in vm:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j-=1
            elif arr[i].lower() not in vm:
                i+=1
            else:
                j-=1
        
        return "".join(arr)
        