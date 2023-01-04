class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hashed={}
        for task in tasks:
            hashed[task] = hashed.get(task, 0)+1
            
        ans=0
        for key in hashed:
            if hashed[key]==1:
                return -1
            c=hashed[key]
            if c%3==0:
                ans+=c//3
            else:
                ans+=1+(c//3)
        return ans