class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = list()
        
        for n in nums:
            if n<pivot:
                ans.append(n)
        
        for n in nums:
            if n==pivot:
                ans.append(n)
        
        for n in nums:
            if n>pivot:
                ans.append(n)
        
        return ans