class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        
        curr = 0
        s=0
        count=0
        for e in range(0, len(arr)):
            curr+=arr[e]
            
            if e >= k-1:
                if curr/k >= t:
                    count+=1
                
                curr-=arr[s]
                s+=1
        
        return count
            