#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		max1=-1
		max2=-1
		
		for n in arr:
		    
		    if n>max1:
		        max2=max1
		        max1=n
		    elif n<max1 and n>max2:
                max2=n
		
		return max2


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends