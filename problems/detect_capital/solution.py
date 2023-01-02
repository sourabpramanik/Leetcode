class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        state=0
        if word[0].isupper():
            state=0
        elif not word[0].isupper():
            state=2
        
        n=len(word)
        for i in range(1, n):
            if state==0:
                if word[i].isupper():
                    state=1
                else:
                    state=2
            elif state==1:
                if word[i].isupper():
                    state=1
                    continue
                else:
                    return False
            elif state==2:
                if not word[i].isupper():
                    state=2
                    continue
                else:
                    return False
        return True


