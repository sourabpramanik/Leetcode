#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        vector=[]
        for i in range(0, len(start)):
            vector.append((start[i], end[i], i+1))
        
        vector.sort(key=lambda x:(x[1], x[2]))
        
        count=1
        preStart=vector[0][0]    
        preEnd=vector[0][1]
        
        for i in range(1, len(vector)):
            if vector[i][0]>preEnd:
                count+=1
                preStart=vector[i][0]    
                preEnd=vector[i][1]
        return count
    


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