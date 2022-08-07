class Solution:
    def reverse(self, x: int) -> int:        
        num = int(str(abs(x))[::-1])
        if( num > 0x7FFFFFFF ):  return 0;
        return num*-1 if x<0 else num