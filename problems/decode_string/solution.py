class Solution:
    def decodeString(self, s: str) -> str:
        stackC = []
        stackW = []
        self.num = 0
        self.word = ""
        
        def rec(i):
            if i==len(s):
                return
            if s[i].isdigit():
                self.num = self.num*10 + int(s[i])
            elif s[i]=="[":
                stackC.append(self.num)
                stackW.append(self.word)
                self.num = 0
                self.word = ""
            elif s[i]=="]":
                count = stackC.pop()
                dup = stackW.pop()
                for j in range(1, count+1):
                    dup += self.word
                
                self.word = dup
            else:
                self.word += s[i]
            
            rec(i+1)
        rec(0)
        
        return self.word
                