class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = dict()
        
        i = 1
        for v in nums:
            diff = target - v
            
            if not diff in hashmap:
                hashmap[v] = i
                i+=1
            else:
                return [hashmap[diff]-1, i-1]
                
     