class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        return self.divide(arr, 0, len(arr)-1)

    def divide(self, arr, l, r):
        if l>=r:
            return 0
        mid=(l+r)>>1
        count=self.divide(arr, l, mid)
        count+=self.divide(arr, mid+1, r)
        count+=self.merge(arr, l, mid, r)
        return count

    def merge(self, arr, left, mid, right):
        j=mid+1
        count=0
        temp=[]
        for i in range(left, mid+1):
            while j<=right and arr[i]>2*arr[j]:
                j+=1
            count+=j-mid-1
        
        i=left
        j=mid+1

        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        
        while i<=mid:
            temp.append(arr[i])
            i+=1
        
        while j<=right:
            temp.append(arr[j])
            j+=1
        
        for i in range(left, right+1):
            arr[i]=temp[i-left]
        
        return count

