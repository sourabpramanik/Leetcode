#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        maxSub=0
        target=0
        hashes={}
        
        for i in range(0, n):
            target+=arr[i]
            if target==0:
                maxSub=i+1
            else:
                if target in hashes:
                    maxSub = max(maxSub, i-hashes[target])
                else:
                    hashes[target] = i
        return maxSub
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends