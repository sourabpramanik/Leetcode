#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        ans=0
        store={}
        preSum=0
        for i in range(0, n):
            preSum+=arr[i]
            if preSum==0:
                ans=i+1
            else:
                if preSum in store:
                    ans=max(ans, i-store[preSum])
                else:
                    store[preSum] = i
        return ans
                    

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