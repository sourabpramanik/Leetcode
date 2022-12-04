#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        ans=1
        arr=[]
        for i in range(0, n):
            arr.append((start[i], end[i], i+1))
        
        arr.sort(key=lambda x:(x[1], x[2]))
        
        preStart=arr[0][0]
        preEnd=arr[0][1]
        for i in range(1, n):
            curStart=arr[i][0]
            curEnd=arr[i][1]
            
            if curStart>preEnd:
                ans+=1
                preStart=curStart
                preEnd=curEnd
        
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends