class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        word=""
        rev=""
        for i in range(n-1, -1, -1):
            ch=s[i]
            if ch!=" ":
                word+=ch
            else:
                if word!="":
                    if rev!="":
                        rev+=" "
                    rev+=word[::-1]
                    word=""
        if word!="":
            if rev!="":
                rev+=" "
            rev+=word[::-1]
        return rev
