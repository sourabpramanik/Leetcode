class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        
        for i in range(0, len(a)):
            
            if a[i][-1]>=target :
                arr=a[i]
                s=0
                e=len(arr)-1
                
                while(s<=e):
                    m = (s+e)//2
                    
                    if arr[m]==target:
                        return True
                    elif arr[m]>target:
                        e=m-1
                    else:
                        s=m+1
        
        return False