#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        jobs=[]
        for i in range(0, n):
            jobs.append([Jobs[i].id, Jobs[i].deadline, Jobs[i].profit])
        
        jobs.sort(key=lambda x: x[2], reverse=True)
        maxDeadline = 0
        for i in range(0, n):
            maxDeadline=max(maxDeadline, jobs[i][1])
        
        days=[-1]*(maxDeadline+1)
        profit=0
        count=0
        for i in range(0, n):
            day=jobs[i][1]
            while day:
                if days[day]==-1:
                    days[day]=jobs[i][0]
                    profit+=jobs[i][2]
                    count+=1
                    break
                else:
                    day-=1
        
        return [count, profit]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends