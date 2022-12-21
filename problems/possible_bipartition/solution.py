class UF:
    def __init__(self, n):
        self.p = [i for i in range(n+1)]
    
    def find(self, i):                                        # Find parent
        if i != self.p[i]:
            self.p[i] = self.find(self.p[i])
        return self.p[i]    
        
    def union(self, j, parent_dislike_i, parent_i):    
        p_j = self.find(j)
        self.p[p_j] = parent_dislike_i 
        return p_j != parent_i                                # Check if there is a parent conflict
        
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)            
        uf = UF(N)
        for (u, v) in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        for i in range(1, N+1):
            parent_i = uf.find(i)
            if parent_i in self.graph:
                parent_dislike_i = uf.find(self.graph[i][0])  
                for dis in self.graph[i][1:]:                
                    if not uf.union(dis, parent_dislike_i, parent_i): return False   
        return True  