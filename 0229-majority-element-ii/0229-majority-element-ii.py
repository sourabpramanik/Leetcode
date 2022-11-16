class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        for k in count:
            if count[k]>len(nums)/3:
                ans.append(k)
        
        return ans