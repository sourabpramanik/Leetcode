class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def rabin( src, pat):   
            if src=="" or pat=="":
                return -1
            d=31
            hash_s=0
            hash_p=0
            base=100000
            power=1
            n=len(src)
            m=len(pat)
            
            for i in range(m):
                power=(power*d)%base
            
            for i in range(m):
                hash_p=(hash_p*d + ord(pat[i])) % base
                

            for i in range(n):
                hash_s=(hash_s*d + ord(src[i])) % base
                if i < m-1:
                    continue
                
                if i >= m:
                    hash_s=(hash_s - ord(src[i-m])*power)%base
                    
                if hash_s<0:
                    hash_s=base

                if hash_s==hash_p:
                    if src[i-m+1:i+1]==pat:
                        return i-m+1
            return -1


        count=1
        s=a
        while len(s)<len(b):
            s+=a
            count+=1

        if s==b:
            return count
        
        if rabin(s, b)!= -1: return count
        if rabin(s+a, b)!= -1: return count+1

        return -1
