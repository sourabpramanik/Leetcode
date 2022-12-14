class Solution:
    def reverseWords(self, s: str) -> str:
        arr=[]
        temp=""

        for i in range(0, len(s)):
            ch=s[i]

            if ch==" ":
                if temp!="":
                    arr.append(temp)
                    temp=""
            else:
                temp+=ch
        if temp!="":
            arr.append(temp)
        return " ".join(arr[::-1])