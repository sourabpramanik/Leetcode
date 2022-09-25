class Solution:
    def sortPeople(self, N: List[str], H: List[int]) -> List[str]:
        for i in range(0, len(H)):
            for j in range(i+1, len(H)):
                if(H[i]<H[j]):
                    H[i], H[j] = H[j], H[i]
                    N[i], N[j] = N[j], N[i]
        
        return N