class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()+" "
        sign = -1 if s[0] == "-" else 1
        p1 = p2 = 1 if(s[0] in ("-", "+")) else 0
        while p2<len(s) and s[p2].isdigit(): p2+=1
        num = sign * int(s[p1 : p2]) if(p2>p1) else 0
        
        if(num> 0x7FFFFFFF): return 2147483647
        if(num < -0x7FFFFFFF): return -2147483648
        return num